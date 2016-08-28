from django.core.management.base import BaseCommand
from django.core.cache import cache


class Command(BaseCommand):

    def handle(self, *args, **options):
        cache.delete_pattern("*")
        self.stdout.write("All cache are cleared.")
