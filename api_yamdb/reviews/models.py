from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from users.models import User
from titles.models import Title


class Review(models.Model):
    text = models.TextField(
        verbose_name='Текст',
    )
    title = models.ForeignKey(
        Title, verbose_name='Произведение',
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews'
    )

    pub_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата публикации', db_index=True
    )

    score = models.PositiveSmallIntegerField(
        validators=(
            MaxValueValidator(10),
            MinValueValidator(1),
        ),
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('pub_date',)
        constraints = (
            models.UniqueConstraint(
                fields=('title', 'author'),
                name='unique_review'
            ),
        )


class Comment(models.Model):
    reviews = models.ForeignKey(Review, on_delete=models.CASCADE,
                                related_name='comments')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField()
    pub_date = models.DateTimeField(
        'date published', auto_now_add=True, db_index=True
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('pub_date',)
