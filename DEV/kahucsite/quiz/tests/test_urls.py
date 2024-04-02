"""Test the urls."""
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from quiz.views import CreateQuizz


class TestUrls(SimpleTestCase):
    """Class response for test urls."""

    def test_create_quizz_url_resolved(self):
        url = reverse("Create a Quizz")
        self.assertEquals(resolve(url).func, CreateQuizz)
