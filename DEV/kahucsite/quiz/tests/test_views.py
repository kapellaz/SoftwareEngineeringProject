"""Test the urls."""
from django.test import TestCase, Client
from django.urls import reverse

filename = "Create a Quizz"


class TestViews(TestCase):
    """Class response for test urls."""

    def test_create_quizz_GET(self):
        client = Client()
        response = client.get(reverse(filename))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'CreateQuizz.html')
