
from django.contrib import admin
from .models import Flashcards
# Register your models here.


# class FlashCards(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question']}),
#         ('Date information', {'fields': ['answer']})
#     ]


admin.site.register(Flashcards)
