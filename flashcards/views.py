from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import Template, Context
from .models import Flashcards
import random
from django.views.generic import ListView, DetailView


# Create your views here.

def random_flashcard(request):
    global flashcard
    number_of_flashcards = Flashcards.objects.count()
    random_id = random.randint(1, number_of_flashcards)
    if 'flashcard_displayed' in request.session:
        if len(request.session['flashcard_displayed']) >= number_of_flashcards:
            return HttpResponse('100 FISZEK PRZEROBINYCH na dzisaj koniec')

        if random_id not in request.session['flashcard_displayed']:
            request.session['flashcard_displayed'].insert(0, random_id)
            flashcard = Flashcards.objects.get(ID=random_id)

        else:
            while random_id in request.session['flashcard_displayed']:
                random_id = random.randint(1, number_of_flashcards)

            request.session['flashcard_displayed'].insert(0, random_id)
            flashcard = Flashcards.objects.get(ID=random_id)

    else:
        random_id = random.randint(1, number_of_flashcards)
        flashcard = Flashcards.objects.get(ID=random_id)
        request.session['flashcard_displayed'] = [random_id]

    request.session.modified = True

    context = {'random_flashcard': flashcard}

    return render(request, 'flashcard.html', context)


class FlashcardsView(ListView):
    template_name = 'main_page.html'
    model = Flashcards


class BlogPageView(ListView):
    template_name = 'Leitner_system.html'
    model = Flashcards


class AboutQuiz(ListView):
    template_name = 'about_quiz.html'
    model = Flashcards


class Ranking(ListView):
    template_name = 'ranking.html'
    model = Flashcards
