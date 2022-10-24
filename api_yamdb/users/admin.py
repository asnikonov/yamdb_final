from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from .models import User


class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'role', 'first_name',
        'last_name', 'is_staff',
    )

    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'role')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2', 'role')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )


admin.site.register(User, CustomUserAdmin)
