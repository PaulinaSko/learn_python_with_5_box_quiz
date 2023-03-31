from django.urls import path
from .views import random_flashcard, FlashcardsView, BlogPageView, AboutQuiz, Ranking


urlpatterns = [
    path('', FlashcardsView.as_view(), name='index'),
    path('Leitner_system/', BlogPageView.as_view(), name='Leitner_system'),
    path('about_quiz/', AboutQuiz.as_view(), name='about_quiz'),
    path('ranking/', Ranking.as_view(), name='ranking'),
    path('flashcards/', random_flashcard, name='flashcard'),
]
