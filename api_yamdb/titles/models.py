from datetime import date
from django.db import models
from django.core.exceptions import ValidationError


class Category(models.Model):
    name = models.CharField('Название категории',
                            max_length=256,
                            blank=False
                            )
    slug = models.SlugField('Уникальный URL',
                            max_length=50,
                            unique=True,
                            db_index=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField('Название жанра', max_length=256, blank=False)
    slug = models.SlugField(unique=True, db_index=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Title(models.Model):
    def year_validation(self):
        if self > date.today().year:
            raise ValidationError(
                ('Неверно указан год.'),
                params={'value': self},
            )
    name = models.CharField('Название', max_length=256, blank=False)
    description = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        verbose_name='Категория',
        null=True
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
        verbose_name='Жанр'
    )
    year = models.IntegerField(
        validators=(year_validation,),
        db_index=True,
    )

    class Meta:

        verbose_name = 'Заголовок'
        verbose_name_plural = 'Заголовки'

    def __str__(self):
        return self.name
