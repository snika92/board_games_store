from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Game, Address
from add_game_script import add_game_script


def home(request):
    games = Game.objects.all()[:3]
    context = {'games': games}
    return render(request, 'store/home.html', context)


def game_details(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    context = {'game': game}
    return render(request, 'store/game_details.html', context)


def games_for_children(request):
    games = Game.objects.filter(category__title='Для детей')
    context = {'games': games}
    return render(request, 'store/for_children.html', context)


def games_for_adults(request):
    games = Game.objects.filter(category__title='Для взрослых')
    context = {'games': games}
    return render(request, 'store/for_adults.html', context)


def games_for_families(request):
    games = Game.objects.filter(category__title='Для всей семьи')
    context = {'games': games}
    return render(request, 'store/for_families.html', context)


def games_all(request):
    games = Game.objects.all()
    context = {'games': games}
    return render(request, 'store/all.html', context)


def contacts(request):
    address = Address.objects.first()
    context = {'address': address}
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'store/contacts.html', context)


def add_game(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.POST.get('image')
        category = request.POST.get('category')
        price = request.POST.get('price')
        game_dict = {
            'title': title,
            'description': description,
            'image': image,
            'category': category,
            'price': price,
        }
        print(f'{title} ({category}): {price}')
        add_game_script(game_dict)
        return render(request, 'store/add_game.html')
    return render(request, 'store/add_game.html')
