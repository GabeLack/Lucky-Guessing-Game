import unittest
from unittest.mock import patch
import datetime

from luckygame import LuckyGame
from details import Details
from main import GameController

class TestGameController(unittest.TestCase):

    def setUp(self):
        """Set up a fresh instance of GameController for each test."""
        self.controller = GameController()

    @patch('builtins.input', side_effect=['J0hn D0e', 'John Doe'])
    @patch('builtins.print')
    def test_input_name(self, mocked_print, mocked_input):
        """Test if input_name() handles an invalid name correctly."""
        self.controller.input_name()
        # Asserting that the input and print functions were called
        mocked_input.assert_any_call("Please input your player name -> ")
        # The first input is invalid, so the second one should be accepted
        self.assertEqual(self.controller.details.name, 'John Doe',
                         "The input_name method should set the player's name.")
        mocked_print.assert_any_call("Please enter a valid name.")
        mocked_print.assert_any_call("Welcome John Doe!")

    @patch('builtins.input', side_effect=['2008-50-50', '2000-01-01'])
    @patch('builtins.print')
    def test_input_birth(self, mocked_print, mocked_input):
        """Test if input_birth() handles an invalid birthdate correctly."""
        self.controller.input_birth()
        # Asserting that the input and print functions were called
        mocked_input.assert_any_call("Please input your birth date: yyyy-mm-dd -> ")
        # The first input is invalid, so the second one should be accepted
        self.assertEqual(self.controller.details.birthdate, datetime.datetime(2000, 1, 1),
                         "The input_birth method should set the player's birthdate.")
        mocked_print.assert_any_call("Please enter a valid birthdate.")
        mocked_print.assert_any_call("Your birthdate is 2000-01-01 and you're 24 years old.")

    @patch('builtins.input', side_effect=['john doe', '2000-01-01', '50', 'N'])
    @patch('builtins.print')
    @patch('luckygame.random.sample', return_value=[30, 35, 40, 45, 50, 55, 60, 65, 70, 75])
    @patch('luckygame.random.choice', return_value=50)
    def test_play_game_win_exit(self, mock_random_choice, mock_random_sample, mocked_print, mocked_input):
        """Test if play_game() runs a game correctly."""
        
        # Set up the controller
        self.controller.input_name()
        self.controller.input_birth()
        
        # Ensure the play_game method is called with the mocked attributes
        self.controller.play_game()

        # Asserting that the input and print functions were called
        mocked_print.assert_any_call("Welcome to the Lucky Number Guessing Game!")
        mocked_print.assert_any_call("Number list: [30, 35, 40, 45, 50, 55, 60, 65, 70, 75]")
        mocked_input.assert_any_call("Which of these in the number list do you think is the lucky number? -> ")
        mocked_print.assert_any_call("Congratulations John Doe! You won after 1 attempt(s)!")
        mocked_input.assert_any_call("Do you want to play again? (Enter 'N' for no, anything else for Yes): ")

    @patch('builtins.input', side_effect=['john doe', '2000-01-01', '40', '45', '55', 'N'])
    @patch('builtins.print')
    @patch('luckygame.random.sample', return_value=[30, 35, 40, 45, 50, 55, 60, 65, 70, 75])
    @patch('luckygame.random.choice', return_value=50) # shorter_lucky_list = [40, 45, 50, 55, 60]
    def test_play_game_lose_exit(self, mock_random_choice, mock_random_sample, mocked_print, mocked_input):
        """Test if play_game() runs a game correctly."""
        
        # Set up the controller
        self.controller.input_name()
        self.controller.input_birth()
        
        # Ensure the play_game method is called with the mocked attributes
        self.controller.play_game()

        # Asserting that the input and print functions were called
        mocked_print.assert_any_call("Welcome to the Lucky Number Guessing Game!")
        mocked_print.assert_any_call("Number list: [30, 35, 40, 45, 50, 55, 60, 65, 70, 75]")
        mocked_input.assert_any_call("Which of these in the number list do you think is the lucky number? -> ")
        mocked_print.assert_any_call("Try again!")
        mocked_print.assert_any_call("Updated number list: [45, 50, 55, 60]")
        mocked_print.assert_any_call("The list has been shortened to 2 or fewer, you lose.")
        mocked_input.assert_any_call("Do you want to play again? (Enter 'N' for no, anything else for Yes): ")

if __name__ == '__main__':
    unittest.main()
