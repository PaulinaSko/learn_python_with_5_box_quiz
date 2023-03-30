
from django.urls import path

from . import views
from django.conf.urls.static import static
from .views import random_flashcard

app_name = 'flashcards'
urlpatterns = [
    path('flashcards/', random_flashcard, name='flashcards'),
]
