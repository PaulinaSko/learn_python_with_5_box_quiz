
from django.contrib import admin
from .models import Flashcards
# Register your models here.

# admin.site.register(Flashcards)


@admin.register(Flashcards)
class Flashcards(admin.ModelAdmin):
    fields = ["question", "answers", "box_ID"]
    list_display = ["ID", "question", "box_ID"]
    list_filter = ["box_ID"]
    search_fields = ["question"]

