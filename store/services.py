from store.models import Game


class GameService:
    @staticmethod
    def get_list_of_games_by_category(category):
        list_of_games = Game.objects.filter(category__title=category)
        return list_of_games
