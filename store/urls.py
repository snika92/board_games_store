from django.urls import path
from store.views import HomeView, ContactFormView, GameDetailView, GamesForChildrenListView, GamesForAdultsListView, \
    GamesForFamiliesListView, GameListView, GameCreateView, GameUpdateView, GameDeleteView
from store.apps import StoreConfig

app_name = StoreConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('game/<int:pk>/', GameDetailView.as_view(), name='game_details'),
    path('games_for_children/', GamesForChildrenListView.as_view(), name='games_for_children'),
    path('games_for_adults/', GamesForAdultsListView.as_view(), name='games_for_adults'),
    path('games_for_families/', GamesForFamiliesListView.as_view(), name='games_for_families'),
    path('games_all/', GameListView.as_view(), name='games_all'),
    path('add_game/', GameCreateView.as_view(), name='add_game'),
    path('game/<int:pk>/edit/', GameUpdateView.as_view(), name='update_game'),
    path('game/<int:pk>/delete/', GameDeleteView.as_view(), name='delete_game'),
    path('contacts/', ContactFormView.as_view(), name='contacts')
]
