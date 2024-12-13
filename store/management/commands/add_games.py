from django.core.management.base import BaseCommand
from django.core.management import call_command
from store.models import Category, Game


class Command(BaseCommand):
    help = 'Load categories and games from fixture'

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        Game.objects.all().delete()
        call_command('loaddata', 'store_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))
