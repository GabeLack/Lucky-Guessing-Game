import unittest
import datetime
from dateutil.relativedelta import relativedelta

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
        self.assertEqual(self.d.name, expected,
                         "The valid name 'John Doe' should be set correctly.")

    def test_in_name_with_multiple_spaces(self):
        # Adaptation:
        self.d.in_name('  Jane    Doe  ')
        # Asserting:
        self.assertIsNone(self.d.name,
                          "Names with numbers extra spaces should be invalid and not set.")

    def test_in_name_with_numbers(self):
        # Adaptation:
        self.d.in_name('John123')
        # Asserting:
        self.assertIsNone(self.d.name,
                          "Names with numbers should be invalid and not set.")

    def test_in_name_empty_string(self):
        # Adaptation:
        self.d.in_name('')
        # Asserting:
        self.assertIsNone(self.d.name,
                          "An empty string should not be a valid name.")

    def test_in_name_with_special_characters(self):
        # Adaptation:
        self.d.in_name('John_Doe')
        # Asserting:
        self.assertIsNone(self.d.name,
                          "Names with special characters should be invalid.")

    def test_in_name_with_apostrophe(self):
        # Adaptation:
        self.d.in_name("John'Doe")
        # Asserting:
        self.assertIsNone(self.d.name,
                          "Names with special characters should be invalid.")

    def test_in_name_accented(self):
        # Adaptation:
        self.d.in_name('José')
        # Asserting:
        self.assertIsNone(self.d.name,
                          "Names with accented characters should be invalid.")

    def test_in_name_long(self):
        # Adaptation:
        self.d.in_name('name with more than one space seperation')
        # Asserting:
        self.assertIsNone(self.d.name,
                          "Names with more than one space separation should be invalid.")

    #! ------------------- TESTS BIRTH ------------------- !
    def test_valid_birth(self):
        # Adaptation:
        self.d.in_birth('1951-01-01')
        expected_age = datetime.datetime.now().year - 1951
        expected_birthdate = datetime.datetime(1951, 1, 1)
        # Asserting:
        self.assertEqual(self.d.age, expected_age,
                         "The age should be calculated correctly.")
        self.assertEqual(self.d.birthdate, expected_birthdate,
                         "The birthdate should be stored correctly as a datetime object.")

    def test_birth_too_young(self):
        # Adaptation:
        self.d.in_birth('2007-01-01')  # Age would be less than 18
        # Asserting:
        self.assertIsNone(self.d.age,
                          "Age should be None if younger than 18.")
        self.assertIsNone(self.d.birthdate,
                          "Birthdate should be None if younger than 18.")

    def test_invalid_birthdate_format(self):
        # Testing an invalid format:
        result = self.d.in_birth('20000101')  # Invalid format, should return None
        # Asserting:
        self.assertIsNone(result,
                          "Invalid date format should return None.")

    def test_birthdate_future(self):
        # Testing a date in the future:
        self.d.in_birth('2026-01-01')  # Future date
        # Asserting:
        self.assertIsNone(self.d.age,
                          "Age should be None if the birthdate is in the future.")
        self.assertIsNone(self.d.birthdate,
                          "Birthdate should be None if the birthdate is in the future.")

    def test_birthdate_leap_year_valid(self):
        # Testing a valid leap year:
        self.d.in_birth('2000-02-29')
        expected_age = datetime.datetime.now().year - 2000
        expected_birthdate = datetime.datetime(2000, 2, 29)
        # Asserting:
        self.assertEqual(self.d.age, expected_age,
                         "Leap year date should be handled correctly.")
        self.assertEqual(self.d.birthdate, expected_birthdate,
                         "The birthdate should be stored correctly as a datetime object.")

    def test_birthdate_non_leap_year(self):
        # Testing an invalid leap year date:
        result = self.d.in_birth('2019-02-29')  # Invalid leap year date
        # Asserting:
        self.assertIsNone(result,
                          "Invalid leap year date should return None.")

    def test_birthdate_exact_18(self):
        # Testing exactly 18 years ago:
        eighteen_years_ago = (datetime.datetime.now() - relativedelta(years=18)).strftime('%Y-%m-%d')
        result = self.d.in_birth(eighteen_years_ago)
        # Asserting:
        self.assertIsNotNone(result,
                            "Exactly 18 years ago should be a valid birthdate.")

    def test_birthdate_almost_18(self):
        # Testing almost 18 years ago:
        almost_18 = (datetime.datetime.now() - datetime.timedelta(days=17*365 + 364)).strftime('%Y-%m-%d')
        result = self.d.in_birth(almost_18)
        # Asserting:
        self.assertIsNone(result,
                          "Almost 18 years ago should be an invalid birthdate.")

if __name__ == '__main__':
    unittest.main()