from django.urls import path

from . import views
from .views import random_flashcard

app_name = 'flashcards'
urlpatterns = [

    path('', random_flashcard),
]
