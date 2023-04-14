from django.contrib import admin
from .models import CustomUser, Profile
# Register your models here.

admin.site.register(CustomUser)


@admin.register(Profile)
class Profile(admin.ModelAdmin):
    fields = ['user', 'bio']
    list_display = ['user']
