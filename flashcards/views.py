from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Flashcards


def hello(request):
    return render(
        request, template_name='hello.html',
    )


class Question(generic):
    model = Flashcards



# Create your views here.
