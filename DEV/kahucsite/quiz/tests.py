from django.test import TestCase
from django.urls import reverse


# Create your tests here.

class BaseTest(TestCase):
    def setUp(self):
        self.create_quizz_url = reverse('Create a Quiz')

        return super().setUp()


class NoLoginTests(BaseTest):
    def test_create_quiz_no_login(self):
        response = self.client.get(self.create_quizz_url)
        self.assertEqual(response.status_code, 302)