from django.test import TestCase
from django.urls import reverse
from .models import Flashcards

# Create your tests here.


class FlashcardsModelTests(TestCase):
    def test_if_flashcard_exist(self):
        response = self.client.get(reverse('flashcards:index'))
        self.assertEqual(response.status_code, 200)

    def test_model_str(self):
        question = Flashcards.objects.create(question="That`s a first question")
        answers = Flashcards.objects.create(answers="No answer")
        self.assertEqual(str(f"Question: {self.question} Answer: {self.answers}"))
        # self.assertEqual(str(answers), "No answer")

