from luckygame import LuckyGame
from details import Details

class GameController:
    def __init__(self):
        self.details = Details()
        self.game = None

    def input_name(self):
        while self.details.name is None:
            input_name = input("Please input your player name -> ")
            name = self.details.in_name(input_name)
            if name:
                print(f"Welcome {name}!")
                break
            else:
                print("Please enter a valid name.")
        return self.details

    def input_birth(self):
        while self.details.birthdate is None:
            input_birth = input("Please input your birth date: yyyy-mm-dd -> ")
            birth = self.details.in_birth(input_birth)
            if birth:
                print(f"Your birthdate is {birth[0].strftime('%Y-%m-%d')} and you're {birth[1]} years old.")
                break
            else:
                print("Please enter a valid birthdate.")
        return self.details

    def play_game(self):
        self.game = LuckyGame(self.details)
        print("Welcome to the Lucky Number Guessing Game!")

        while True:
            self.game.generate_new_game()
            print(f"Number list: {self.game.lucky_list}")
            tries = 0  # Reset tries for each game

            game_over = False
            while not game_over:
                player_input = input("Which of these in the number list do you think is the lucky number? -> ")
                tries, result_message = self.game.play_round(player_input, tries)
                print(result_message)

                # If the game is not over, show the updated number list
                if "Congratulations" in result_message or "you lose" in result_message:
                    game_over = True
                else:
                    print(f"Updated number list: {self.game.lucky_list}")

            play_again = input("Do you want to play again? (Enter 'N' for no, anything else for Yes): ").strip().lower()
            if play_again == "n":
                break

if __name__ == '__main__':
    controller = GameController()
    controller.input_name()
    controller.input_birth()
    controller.play_game()
