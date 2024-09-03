from luckygame import LuckyGame
from details import Details

if __name__ == '__main__':
    details = Details()

    while details.name is None:
        input_name = input("Please input your player name -> ")
        name = details.in_name(input_name)
        if name: # if name is not None
            print(f"Welcome {name}!")
            break
        else:
            print("Please enter a valid name.")

    while details.birthdate is None:
        input_birth = input("Please input your birth date: yyyy-mm-dd -> ")
        birth = details.in_birth(input_birth)
        if birth: # if birth is not None
            print(f"Your birthdate is {birth[0].strftime('%Y-%m-%d')} and you're {birth[1]} years old.")
            break
        else:
            print("Please enter a valid birthdate.")


    game = LuckyGame()
    game.game_logic(details.name)
