import os
from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = "Local API to retrieve realtime quotes"

    def handle(self, *args, **options):
        filename = options['filename']
        os.environ["CSV_FILENAME"] = filename
        call_command('runserver',  '0.0.0.0:8000')

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str)