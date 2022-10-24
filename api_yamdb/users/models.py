from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):

    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        choices=settings.ROLE_CHOICES,
        max_length=20,
        blank=False,
        verbose_name='User role',
        help_text='Describes users permissions',
        default=settings.ROLES['user']
    )
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    username = models.CharField(
        'User name',
        max_length=150,
        unique=True,
        validators=[RegexValidator(
            regex=r'^[\w.@+-]+$',
            message='Username must be Alphanumeric',
            code='invalid_username')
        ]
    )
    email = models.EmailField('Email', max_length=254, unique=True)
    confirmation_code = models.CharField(
        'Confirmation code',
        max_length=100,
        null=True
    )

    def __str__(self):
        return str(self.username)

    @property
    def is_admin(self):
        return self.role == settings.ROLES['admin'] or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == settings.ROLES['moderator']

    @property
    def is_user(self):
        return self.role == settings.ROLES['user']

    class Meta:
        ordering = ['username']
