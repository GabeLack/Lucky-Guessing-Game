import random

class LuckyGame():
    def __init__(self) -> None:
        pass

    def generate_new_game(self):
        """
        Generate a new game with a lucky number and a list of 10 random numbers.

        Returns:
            tuple: A tuple containing a list of 10 random numbers, the lucky number,
            and a shorter list of numbers near the lucky number.

        Notes:
            This function ensures that the generated game does not have an extremely
            short list of numbers near the lucky number. If the list becomes too short,
            it will regenerate the game to provide a reasonable challenge.
        """
        lucky_list = random.sample(range(1, 101), 10)
        lucky_number = random.choice(lucky_list)
        shorter_lucky_list = [i for i in lucky_list if lucky_number + 10 > i > lucky_number - 10]

        # Prevent the game from running TOO short, calls function again if so
        if len(shorter_lucky_list) <= 3:
            return self.generate_new_game()
        
        return lucky_list, lucky_number, shorter_lucky_list
    
    def valid_guess(self, number_list, tries):
        """
        Get a valid guess from the player.

        Args:
            number_list (list): The list of valid numbers to guess from.
            tries (int): The current number of tries.

        Returns:
            tuple: A tuple containing the player's valid guess and the updated number of tries.
        """
        player_input = None
        while player_input is None:
            guess = input("Which of these in the number list do you think is the lucky number? -> ")
            # Check if the guess is numeric and within the valid number list.
            if guess.isnumeric() and int(guess) in number_list:
                player_input = int(guess)
                tries += 1  # Increment tries for a valid guess
            else:
                print("Not a valid guess")
                tries += 1  # Increment tries for an invalid guess
        return player_input, tries
    
    def check_count(self, shorter_lucky_list):
        """
        Check if the list has become too short for the player to continue.

        Args:
            shorter_lucky_list (list): The list of remaining numbers.

        Returns:
            bool: True if the list is too short, indicating a loss; False otherwise.
        """
        if len(shorter_lucky_list) <= 2:
            # If the list becomes too short, the player loses.
            print("The list has been shortened to 2 or fewer, you lose.")
            return True
        
    def check_win(self, input, lucky_number, tries, name):
        """
        Check if the player has guessed the correct lucky number and won the game.

        Returns:
            bool: True if the player has won, False otherwise.
        """
        if input == lucky_number:
            # Player guessed the correct lucky number.
            print(f"Congratulations {name}! You won after {tries} number of tries!")
            return True
    
    def play_round(self, name):
        """
        Play a round of the Lucky Number Guessing Game.

        Args:
            name (str): The player's name.

        This method initiates a new round of the game, where the player guesses a lucky number.
        The game continues until the player guesses the lucky number or the list becomes too short.
        The number of tries taken to guess the lucky number is recorded and displayed at the end.

        Returns:
            None
        """
        # Generate a new game by selecting a lucky number and a list of 10 random numbers.
        lucky_list, lucky_number, shorter_lucky_list = self.generate_new_game()
        # Initialize the number of tries taken by the player.
        tries = 0
        # Display the full list of lucky numbers to the player.
        print(f"Number list: {lucky_list}")

        # The game loop continues until the player wins or loses.
        while True:
            # Prompt the player for their guess and increment the number of tries.
            player_input,tries = self.valid_guess(lucky_list,tries)

            if self.check_win(player_input, lucky_number, tries, name):
               # if True, they won, then break
               break
            else:
                # Player guessed a number in the lucky list but not the correct one.

                # Remove from shorter lucky list if guess was present there too
                if player_input in shorter_lucky_list:
                    shorter_lucky_list.remove(player_input)

                print(f"Number list: {shorter_lucky_list}")

                # Check if the list length is lower than 3 using the check_count method.
                if self.check_count(shorter_lucky_list):
                    break

                # Prompt the player for another guess using the valid_guess method.
                player_input,tries = self.valid_guess(shorter_lucky_list,tries)

                if self.check_win(player_input, lucky_number, tries, name): 
                    # if True, they won, then break
                    break
                else:
                    # Player guessed a valid number, but it's not the correct one.
                    shorter_lucky_list.remove(player_input)
                    print(f"Number list: {shorter_lucky_list}")

                    # Check if the list length is lower than 3 using the check_count method.
                    if self.check_count(shorter_lucky_list):
                        break
        
    def game_logic(self, name):
        """
        Run the Lucky Number Guessing Game.

        Args:
            name (str): The player's name.

        Manages the game's flow, continuously prompting the player for rounds
        until they choose to exit.

        Returns:
            None
        """
        print("Welcome to the Lucky Number Guessing Game!")

        while True:  # Loops as long as the user wants to play
            self.play_round(name)
            play_again = input("Do you want to play again? (Enter 'N' for no, anything else for Yes): ").strip().lower()
            if play_again == "n": 
                break