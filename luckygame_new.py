import random
from details import Details

class LuckyGame:
    def __init__(self, details:Details) -> None:
        self.details = details
        self.generate_new_game()

    def generate_new_game(self):
        """
        Generate a new game with a lucky number and a list of 10 random numbers.
        """
        self.lucky_list = random.sample(range(1, 101), 10)
        self.lucky_number = random.choice(self.lucky_list)
        self.shorter_lucky_list = [i for i in self.lucky_list if 
                                   self.lucky_number + 10 > i > self.lucky_number - 10]

        if len(self.shorter_lucky_list) <= 3: # Prevents the game from running too short
            return self.generate_new_game()

    def valid_guess(self, number_list, player_input):
        """
        Validate the player's guess.
        """
        if player_input.isnumeric() and int(player_input) in number_list:
            return int(player_input)
        else:
            return None

    def play_round(self, player_input, tries):
        """
        Play a round of the Lucky Number Guessing Game.
        """
        valid_guess = self.valid_guess(self.lucky_list, player_input)

        if valid_guess is not None:
            tries += 1 # Increment tries for a valid guess

            if valid_guess == self.lucky_number: # Check if the guess is correct
                result_message = f"Congratulations {self.details.name}! You won after {tries} attempt(s)!"
                return tries, result_message

            else:

                if valid_guess in self.shorter_lucky_list: # Remove the guess from the list
                    self.shorter_lucky_list.remove(valid_guess)


                if len(self.shorter_lucky_list) < 3: # Check if the list is too short
                    result_message = "The list has been shortened to 2 or fewer, you lose."
                    return tries, result_message

                else: # Continue the game if the guess is incorrect
                    self.lucky_list = self.shorter_lucky_list.copy()
                    result_message = "Try again!"
                    return tries, result_message
        else:
            result_message = "Not a valid guess"
            tries += 1
            return tries, result_message
