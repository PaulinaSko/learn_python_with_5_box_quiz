from django.urls import path
from .views import random_flashcard, FlashcardsView, BlogPageView


urlpatterns = [
    path('', FlashcardsView.as_view(), name='index'),
    path('flashcards/', BlogPageView.as_view(), name='Leitner_system'),
    path('flashcards/', random_flashcard, name='flashcard'),
]
