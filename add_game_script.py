from store.models import Game


def add_game_script(values_dict):
    game = Game(title=values_dict['title'], description=values_dict['description'], image=values_dict['image'],
                category_id=values_dict['category'], price=values_dict['price'])
    game.save()
