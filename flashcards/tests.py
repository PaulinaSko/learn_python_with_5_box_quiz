from django.test import TestCase
from django.urls import reverse
from .models import Flashcards


# Create your tests here.


class FlashcardsPagesTests(TestCase):
    # check if URL works correctly and the / web page, the homepage, returns an HTTP 200 Response
    def test_url_flashcard_at_current_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # confirm calling the page by its URL name via reverse()
    def test_url_flashcard_available_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    # check the tamplate`s content looking for the HTML snippet <h1> and that incorrect HTML is not on the page
    def test_template_about_quiz_content(self):
        response = self.client.get(reverse('about_quiz'))
        self.assertContains(response, "<h1>Few words about 5_box_quiz - how it`s working?</h1>")
        self.assertNotContains(response, "Not on the page")


class FlashcardsModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.question = Flashcards.objects.create(question="That`s a first question")
        cls.answers = Flashcards.objects.create(answers="No answer")

    # checks that data in our mock database matches what was initially created in setUpTestData
    def test_model_content(self):
        self.assertEqual(self.question.question, "That`s a first question")
        self.assertEqual(self.answers.answers, "No answer")
