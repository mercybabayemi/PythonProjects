from unittest import TestCase
from classtask import gradingprogram


class MyTestCase(TestCase):
    def test_that_function_exist(self):
        student_scores = {"Gloria":88, "Divine":78, "Esther":65, "Mercy":75, "Uzo":71}
        gradingprogram.get_student_grade(student_scores)
    def test_something(self):
        student_scores = {"Gloria": 88, "Divine": 78, "Esther": 65, "Mercy": 75, "Uzo": 71}
        actual = gradingprogram.get_student_grade(student_scores)
        expected = ["Exceeds Expectations", "Acceptable", "Fail", "Acceptable", "Acceptable"]
        self.assertEqual(actual, expected)
    def test_that_test_raises_exception_with_invalid_input(self):
        student_scores = {"Gloria": 88, "Divine": 78, "Esther": 65, "Mercy": 75, "Uzo": 71}
        self.assertRaises(TypeError, gradingprogram.get_student_grade(student_scores), "moses")