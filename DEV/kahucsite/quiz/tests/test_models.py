"""Test for models."""
from django.test import TestCase
from quiz.models import Quiz, Option


class TestModels(TestCase):
    """Class response for model tests."""

    def setUp(self):
        self.quiz1 = Quiz(
            'Question1',
            'Description1'
        )
        self.quiz2 = Quiz(
            'Question2',
            None
        )
        self.answer1 = Option(
            quiz=self.quiz1,
            answer='Answer1',
            option=True,
            reason='Just because'
        )

    def test_quiz_model(self):
        """This method tests the case: when the user puts a description."""
        self.assertEquals(self.quiz1.question, 'Question1')
        self.assertEquals(self.quiz1.description, 'Description1')
        self.assertEquals(self.quiz1.state, 'À espera de revisão')

    def test_quiz_model_empty_description(self):
        """This method tests the case:
           when the user doesn't put a description."""
        self.assertEquals(self.quiz2.question, 'Question2')
        self.assertIsNone(self.quiz2.description)
        self.assertEquals(self.quiz2.state, 'À espera de revisão')

    def test_alinea_model(self):
        """This method is a simple insertion into the model."""
        self.assertEquals(self.answer1.answer, 'Answer1')
        self.assertTrue(self.answer1.option)
        self.assertEquals(self.answer1.reason, 'Just because')
