from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import GameForm
from .models import Game, Address


class HomeView(TemplateView):
    template_name = 'store/home.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Game.objects.all()[:3]
        return context_data


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
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(category__title='Для детей')
        return queryset


class GamesForAdultsListView(ListView):
    model = Game
    template_name = 'store/for_adults.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(category__title='Для взрослых')
        return queryset


class GamesForFamiliesListView(ListView):
    model = Game
    template_name = 'store/for_families.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(category__title='Для всей семьи')
        return queryset


class ContactFormView(TemplateView):
    model = Address
    context_object_name = "address"
    template_name = 'store/contacts.html'
    success_url = reverse_lazy("store:contacts")


class GameCreateView(CreateView):
    model = Game
    form_class = GameForm
    template_name = 'store/add_game.html'
    success_url = reverse_lazy('store:games_all')


class GameUpdateView(UpdateView):
    model = Game
    form_class = GameForm
    template_name = 'store/add_game.html'
    success_url = reverse_lazy('store:games_all')


class GameDeleteView(DeleteView):
    model = Game
    template_name = 'store/delete_game.html'
    success_url = reverse_lazy('store:games_all')