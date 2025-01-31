from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .services import GameService
from .forms import GameForm, GameModeratorForm
from .models import Game, Address


class HomeView(TemplateView):
    template_name = 'store/home.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Game.objects.filter(is_published=True).all()[:3]
        return context_data


@method_decorator(cache_page(60*15), name='dispatch')
class GameDetailView(DetailView):
    model = Game
    template_name = 'store/game_details.html'
    context_object_name = "game"


class GameListView(ListView):
    model = Game
    template_name = 'store/all.html'
    context_object_name = "games"


class GamesForChildrenListView(ListView):
    model = Game
    template_name = 'store/for_children.html'

    def get_queryset(self, *args, **kwargs):
        queryset = GameService.get_list_of_games_by_category('Для детей')
        return queryset


class GamesForAdultsListView(ListView):
    model = Game
    template_name = 'store/for_adults.html'

    def get_queryset(self, *args, **kwargs):
        queryset = GameService.get_list_of_games_by_category('Для взрослых')
        return queryset


class GamesForFamiliesListView(ListView):
    model = Game
    template_name = 'store/for_families.html'

    def get_queryset(self, *args, **kwargs):
        queryset = GameService.get_list_of_games_by_category('Для всей семьи')
        return queryset


class ContactFormView(TemplateView):
    model = Address
    template_name = 'store/contacts.html'
    # context_object_name = "address"
    # success_url = reverse_lazy("store:contacts")

    def get(self, request):
        address = Address.objects.first()
        context = {'address': address}

        return render(request, 'store/contacts.html', context)

    def post(self, request):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")


class GameCreateView(LoginRequiredMixin, CreateView):
    model = Game
    form_class = GameForm
    template_name = 'store/add_game.html'
    success_url = reverse_lazy('store:games_all')

    def form_valid(self, form):
        game = form.save()
        user = self.request.user
        game.owner = user
        game.save()
        return super().form_valid(form)


class GameUpdateView(LoginRequiredMixin, UpdateView):
    model = Game
    form_class = GameForm
    template_name = 'store/add_game.html'
    success_url = reverse_lazy('store:games_all')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return GameForm
        if user.has_perm('store.can_unpublish_product'):
            return GameModeratorForm
        raise PermissionDenied


class GameDeleteView(LoginRequiredMixin, DeleteView):
    model = Game
    template_name = 'store/delete_game.html'
    success_url = reverse_lazy('store:games_all')

    def delete(self, request, pk):
        game = get_object_or_404(Game, id=pk)
        if not request.user.has_perm('store.delete_product') and not request.user == game.owner:
            raise PermissionDenied

        game.delete()
        # return redirect("store:games_all")
