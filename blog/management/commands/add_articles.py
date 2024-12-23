from django.core.management.base import BaseCommand
from django.core.management import call_command
from blog.models import Blog


class Command(BaseCommand):
    help = 'Load categories and games from fixture'

    def handle(self, *args, **kwargs):
        Blog.objects.all().delete()
        call_command('loaddata', 'blog_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))
