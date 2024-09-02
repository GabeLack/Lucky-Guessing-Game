import unittest
import datetime

from details import Details

class TestDetails(unittest.TestCase):

    def setUp(self):
        """Set up a fresh instance of Details for each test."""
        # Instancing
        self.d = Details()

#! ------------------- TESTS NAME ------------------- !#
    def test_in_name(self):
        # Adaptation:
        self.d.in_name('John Doe')
        expected = 'John Doe'
        # Asserting:
        self.assertEqual(self.d.name, expected, "The valid name 'John Doe' should be set correctly.")

    def test_in_name_with_multiple_spaces(self):
        # Adaptation:
        self.d.in_name('  Jane    Doe  ')
        expected = 'Jane Doe'
        # Asserting:
        self.assertEqual(self.d.name, expected, "The name should be trimmed and formatted correctly.")

    def test_in_name_with_numbers(self):
        # Adaptation:
        self.d.in_name('John123')
        # Asserting:
        self.assertIsNone(self.d.name, "Names with numbers should be invalid and not set.")

    def test_in_name_empty_string(self):
        # Adaptation:
        self.d.in_name('')
        # Asserting:
        self.assertIsNone(self.d.name, "An empty string should not be a valid name.")

    def test_in_name_with_special_characters(self):
        # Adaptation:
        self.d.in_name('John_Doe')
        # Asserting:
        self.assertIsNone(self.d.name, "Names with special characters should be invalid.")

#! ------------------- TESTS BIRTH ------------------- !#
    def test_birth(self):
        # Adaptation:
        self.d.in_birth('19510101')
        expected_age = datetime.datetime.now().year - 1951
        # Asserting:
        self.assertEqual(self.d.age, expected_age, "The age should be calculated correctly.")

    def test_birth_young(self):
        # Adaptation:
        self.d.in_birth('20070101')
        # Asserting:
        self.assertIsNone(self.d.age, "Can't be younger than 18.")

if __name__ == '__main__':
    unittest.main()
