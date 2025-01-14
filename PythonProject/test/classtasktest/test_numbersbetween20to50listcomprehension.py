from unittest import TestCase
from classtask import numbersbetween20to50listcomprehension

class TestListComprehensionFunction(TestCase):
    def test_that_function_exist(self):
        numbers = [12,15,19,21,50,70]
        numbersbetween20to50listcomprehension.get_numbers(numbers)

        def test_that_function_return_correct_value(self):
            actual = numbersbetween20to50listcomprehension.get_numbers(numbers)
            expected = [21,50]
            self.assertEqual(actual, expected)



