from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Flashcards
import random
from django.views.generic import ListView


class Question(generic.DetailView):
    model = Flashcards
    template_name = 'flashcards/flashcard.html'


# Create your views here.

def random_flashcard(request):
    selected_answer = []
    number_of_flashcards = Flashcards.objects.count()

    while len(selected_answer) < number_of_flashcards:
        random_id = random.randint(1, number_of_flashcards)
        random_flashcard_item = Flashcards.objects.get(id=random_id)
        if random_flashcard_item not in selected_answer:
            selected_answer.append(random_flashcard_item)
            return render(request, 'flashcards/flashcard.html', {'random_flashcard': random_flashcard_item})


class FlashcardsView(ListView):
    template_name = 'main_page.html'
    model = Flashcards
