from django.urls import path
from store.views import home, contacts, game_details, games_for_children, games_for_adults, games_for_families, \
    games_all, add_game
from store.apps import StoreConfig

app_name = StoreConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('game_details/<int:game_id>/', game_details, name='game_details'),
    path('games_for_children/', games_for_children, name='games_for_children'),
    path('games_for_adults/', games_for_adults, name='games_for_adults'),
    path('games_for_families/', games_for_families, name='games_for_families'),
    path('games_all/', games_all, name='games_all'),
    path('add_game/', add_game, name='add_game'),
    path('contacts/', contacts, name='contacts')
]
