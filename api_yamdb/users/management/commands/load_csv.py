import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from users.models import User
from titles.models import Genre, Title, Category
from reviews.models import Review, Comment


class Command(BaseCommand):
    def handle(self, *args, **options):
        CGR = '\033[92m'
        CYELL = '\033[93m'
        CEND = '\033[0m'

        data_dir = os.path.join(settings.BASE_DIR, 'static/data/')
        print('=============== Loading csv files do database ===============')
        with open(data_dir + 'users.csv', encoding="utf-8-sig") as csvfile:
            reader = csv.DictReader(csvfile)
            print('Loading' + CYELL + ' users.csv ' + CEND + 'file')
            for row in reader:
                record = User(
                    id=row['id'],
                    username=row['username'],
                    email=row['email'],
                    role=row['role'],
                    bio=row['bio'],
                    first_name=row['first_name'],
                    last_name=row['last_name']
                )
                record.save()

        print('Loading' + CYELL + ' categoty.csv ' + CEND + 'file')
        with open(data_dir + 'category.csv', encoding="utf-8-sig") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                record = Category(
                    id=row['id'],
                    name=row['name'],
                    slug=row['slug']
                )
                record.save()

        print('Loading' + CYELL + ' genre.csv ' + CEND + 'file')
        with open(data_dir + 'genre.csv', encoding="utf-8-sig") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                record = Genre(
                    id=row['id'],
                    name=row['name'],
                    slug=row['slug']
                )
                record.save()

        print('Loading' + CYELL + ' titles.csv ' + CEND + 'file')
        with open(data_dir + 'titles.csv', encoding="utf-8-sig") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                record = Title(
                    id=row['id'],
                    name=row['name'],
                    year=row['year'],
                    category=Category.objects.get(id=row['category'])
                )
                record.save()

        print('Loading' + CYELL + ' genre_title.csv ' + CEND + 'file')
        with open(data_dir + 'genre_title.csv',
                  encoding="utf-8-sig") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                title = Title.objects.get(id=row['title_id'])
                genre = Genre.objects.get(id=row['genre_id'])
                title.genre.set([genre])
                title.save()

        print('Loading' + CYELL + ' review.csv ' + CEND + 'file')
        with open(data_dir + 'review.csv', encoding="utf-8-sig") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                record = Review(
                    id=row['id'],
                    title=Title.objects.get(id=row['title_id']),
                    text=row['text'], author=User.objects.get(
                        id=row['author']),
                    score=row['score'], pub_date=row['pub_date']
                )
                record.save()

        print('Loading' + CYELL + ' comments.csv ' + CEND + 'file')
        with open(data_dir + 'comments.csv', encoding="utf-8-sig") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                record = Comment(
                    id=row['id'],
                    reviews=Review.objects.get(id=row['review_id']),
                    text=row['text'],
                    author=User.objects.get(id=row['author']),
                    pub_date=row['pub_date']
                )
                record.save()

        print('===== Files loading' + CGR + ' complete.' + CEND + '=====')
