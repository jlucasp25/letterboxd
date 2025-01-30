import csv
from django.core.management.base import BaseCommand
from movies.models import Movie


class Command(BaseCommand):
    help = 'Imports movies data from a CSV file into the Movie model.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file']

        try:
            with open(csv_file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    title = row['title']
                    year = int(row['year'])
                    genre = int(row['genre'])
                    movie = Movie(title=title, year=year, genre=genre)
                    movie.save()

                self.stdout.write(self.style.SUCCESS('Successfully imported movies from CSV.'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'CSV file {csv_file_path} not found.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error importing movies: {str(e)}'))
