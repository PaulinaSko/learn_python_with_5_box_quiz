from django.urls import path
from .views import random_flashcard, FlashcardsView, BlogPageView, AboutQuiz, Ranking, show_certificate

urlpatterns = [
    path('', FlashcardsView.as_view(), name='index'),
    path('leitner_system/', BlogPageView.as_view(), name='leitner_system'),
    path('about_quiz/', AboutQuiz.as_view(), name='about_quiz'),
    path('ranking/', Ranking.as_view(), name='ranking'),
    path('flashcards/', random_flashcard, name='flashcard'),
    path('pdf/', show_certificate, name='certificate'),
]
