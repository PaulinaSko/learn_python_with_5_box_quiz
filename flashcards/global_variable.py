from .models import Flashcards
import random

number_of_flashcards = Flashcards.objects.count()
random_id = random.randint(1, number_of_flashcards)
flashcard = Flashcards.objects.get(ID=random_id)


def set_global():
    global flashcard
