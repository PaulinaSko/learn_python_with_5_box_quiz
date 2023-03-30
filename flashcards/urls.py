from django.urls import path
from .views import random_flashcard, FlashcardsView

app_name = 'flashcards'
urlpatterns = [
    path('', FlashcardsView.as_view(), name='index'),
    path('flashcards/', random_flashcard, name='flashcard'),
]
