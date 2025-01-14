from unittest import TestCase
from classtask import evenfromstring


class MyTestCase(TestCase):
    def test_that_function_exist(self):
        message = "73H2AdsdF439dm"
        evenfromstring.get_even_from_string(message)

    def test_that_function_return_correct_value(self):
        message = "73H2AdsdF439dm"
        actual = evenfromstring.get_even_from_string(message)
        expected = [2,4]
        self.assertEqual(actual, expected)


