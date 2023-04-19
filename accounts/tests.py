from django.contrib.auth import get_user_model, authenticate
from django.test import TestCase

# Create your tests here.


class CreateUser(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(username='test', email='test@example.com',
                                                         password='123test123')
        self.user.save()

    def tearDown(self) -> None:
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='test', email='test@example.com', password='123test123')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', email='test@example.com')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username='test', email='wrong@example.com')
        self.assertFalse((user is not None) and user.is_authenticated)

