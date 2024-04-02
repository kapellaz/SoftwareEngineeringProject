"""A."""
from django.test import TestCase
from quiz.forms import NewQuizz


class TestForms(TestCase):
    """This class test the forms."""
    def test_form_pretty_data(self):
        """This method tests the case:
           the user puts the correct form."""
        form = NewQuizz(data={
            'question': 'Question',
            'description': 'Description',

            'answer1': 'Option1',
            'reason1': 'Description1',
            'option1': 'True',

            'answer2': 'Option2',
            'reason2': 'Description2',
            'option2': 'False',

            'answer3': 'Option3',
            'reason3': 'Description3',
            'option3': 'False',

            'answer4': 'Option4',
            'reason4': 'Description4',
            'option4': 'False',

            'answer5': 'Option5',
            'reason5': 'Description5',
            'option5': 'False',

            'answer6': 'Option6',
            'reason6': 'Description6',
            'option6': 'False',
            })

        self.assertTrue(form.is_valid())
        self.assertFalse(form.errors)
        self.assertEquals(len(form.errors), 0, len(form.errors))

    def test_form_values_data(self):
        """This method tests the case:
           the user puts more than one True."""
        form = NewQuizz(data={
            'question': 'Question',
            'description': 'Description',

            'answer1': 'Option1',
            'reason1': 'Description1',
            'option1': 'True',

            'answer2': 'Option2',
            'reason2': 'Description2',
            'option2': 'True',

            'answer3': 'Option3',
            'reason3': 'Description3',
            'option3': 'False',

            'answer4': 'Option4',
            'reason4': 'Description4',
            'option4': 'False',

            'answer5': 'Option5',
            'reason5': 'Description5',
            'option5': 'False',

            'answer6': 'Option6',
            'reason6': 'Description6',
            'option6': 'False',
            })

        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)
        self.assertEquals(len(form.errors), 1, len(form.errors))

    def test_form_just_false(self):
        """This method tests the case:
           the user doesn't put any True value."""
        form = NewQuizz(data={
            'question': 'Question',
            'description': 'Description',

            'answer1': 'Option1',
            'reason1': 'Description1',
            'option1': 'False',

            'answer2': 'Option2',
            'reason2': 'Description2',
            'option2': 'False',

            'answer3': 'Option3',
            'reason3': 'Description3',
            'option3': 'False',

            'answer4': 'Option4',
            'reason4': 'Description4',
            'option4': 'False',

            'answer5': 'Option5',
            'reason5': 'Description5',
            'option5': 'False',

            'answer6': 'Option6',
            'reason6': 'Description6',
            'option6': 'False',
            })

        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)
        self.assertEquals(len(form.errors), 1, len(form.errors))

    def test_form_without_description(self):
        """This method tests the case:
           the user doesn't put description."""
        form = NewQuizz(data={
            'question': 'Question',
            'description': 'Description',

            'answer1': 'Option1',
            'reason1': 'Description1',
            'option1': 'True',

            'answer2': 'Option2',
            'reason2': 'Description2',
            'option2': 'False',

            'answer3': 'Option3',
            'reason3': 'Description3',
            'option3': 'False',

            'answer4': 'Option4',
            'reason4': 'Description4',
            'option4': 'False',

            'answer5': 'Option5',
            'reason5': 'Description5',
            'option5': 'False',

            'answer6': 'Option6',
            'reason6': 'Description6',
            'option6': 'False',
            })

        self.assertTrue(form.is_valid())
        self.assertFalse(form.errors)
        self.assertEquals(len(form.errors), 0, len(form.errors))

    def test_form_empty_data(self):
        """This method tests the case:
           the forms is empty."""
        form = NewQuizz()
        self.assertFalse(form.is_valid())
        self.assertFalse(form.errors)
