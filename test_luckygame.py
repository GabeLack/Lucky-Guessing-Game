import unittest

from luckygame import LuckyGame
from details import Details

class TestLuckyGame(unittest.TestCase):

    def setUp(self):
        """Set up a fresh instance of LuckyGame for each test."""
        # Instancing
        self.d = Details()
        self.d.in_name('John Doe')
        self.d.in_birth('2000-01-01')
        self.lg = LuckyGame(self.d)

    def test_init(self):
        # Adaptation:
        expected = self.d
        # Asserting:
        self.assertEqual(self.lg.details, expected,
                         "The Details instance should be set correctly.")

    def test_generate_new_game(self):
        # Adaptation:
        self.lg.generate_new_game()
        # Asserting:
        self.assertEqual(len(self.lg.lucky_list), 10,
                         "The lucky list should have 10 elements.")
        self.assertTrue(max(self.lg.lucky_list) <= 100,
                        "The lucky list should have elements less than 100.")
        self.assertTrue(min(self.lg.lucky_list) >= 1,
                        "The lucky list should have elements greater than 1.")
        self.assertIn(self.lg.lucky_number, self.lg.lucky_list,
                      "The lucky number should be in the lucky list.")

        self.assertGreater(len(self.lg.shorter_lucky_list), 3,
                           "The shorter lucky list should have more than 3 elements.")
        self.assertTrue(all([self.lg.lucky_number + 10 > i > self.lg.lucky_number - 10
                             for i in self.lg.shorter_lucky_list]),
                        "The shorter lucky list should have elements within 10 of the lucky number.")

    def test_valid_guess(self):
        # Adaptation:
        valid_guess = self.lg.valid_guess(str(self.lg.lucky_number))
        # Asserting:
        self.assertEqual(valid_guess, self.lg.lucky_number,
                         "The valid guess should be the lucky number.")

    def test_valid_guess_wrong(self):
        # Adaptation:
        valid_guess = self.lg.valid_guess('0') # Since 1-100 is the range, 0 is invalid
        # Asserting:
        self.assertIsNone(valid_guess,
                          "The invalid guess should be None.")

    def test_play_round_correct(self):
        # Adaptation:
        tries, result_message = self.lg.play_round(str(self.lg.lucky_number), 0)
        # Asserting:
        self.assertEqual(tries, 1,
                         "The number of tries should be incremented.")
        expected_message = f"Congratulations {self.d.name}! You won after 1 attempt(s)!"
        self.assertIn(expected_message, result_message,
                      "The result message should congratulate the player.")

    def test_play_round_invalid(self):
        # Adaptation:
        tries, result_message = self.lg.play_round('0', 0)
        # Asserting:
        expected_message = "Not a valid guess"
        self.assertIn(expected_message, result_message,
                      "The result message should prompt the player to try again.")

    def test_play_round_incorrect(self):
        # Adaptation:
        tries, result_message = self.lg.play_round(str(self.lg.lucky_list[0]), 0)
        # Asserting:
        expected_message = "Try again!"
        self.assertIn(expected_message, result_message,
                      "The result message should prompt the player to try again.")

    def test_play_round_lose(self):
        # Adaptation:
        self.lg.shorter_lucky_list = self.lg.shorter_lucky_list[:2] # Shorten the list to 2 elements
        tries, result_message = self.lg.play_round(str(self.lg.lucky_list[0]), 0)
        # Asserting:
        expected_message = "The list has been shortened to 2 or fewer, you lose."
        self.assertIn(expected_message, result_message,
                      "The result message should inform the player they lost.")

    def test_play_round_remove_guess(self):
        # Adaptation:
        guessed_number = str(self.lg.lucky_list[0])
        self.lg.play_round(guessed_number, 0)
        # Asserting:
        self.assertNotIn(int(guessed_number), self.lg.shorter_lucky_list,
                        "The guess should be removed from the shorter lucky list.")

    def test_play_round_remove_guess_shorter(self):
        # Adaptation:
        guessed_number = str(self.lg.shorter_lucky_list[0])
        self.lg.play_round(guessed_number, 0)
        # Asserting:
        self.assertNotIn(int(guessed_number), self.lg.shorter_lucky_list,
                        "The guess should be removed from the shorter lucky list.")

if __name__ == '__main__':
    unittest.main()
