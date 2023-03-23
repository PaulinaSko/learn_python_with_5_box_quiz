from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin

from accounts.models import CustomUser

# Register your models here.


class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'last_name', 'first_name',
    )


admin.site.register(CustomUser, CustomUserAdmin)
