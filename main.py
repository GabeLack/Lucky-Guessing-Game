from luckygame import LuckyGame
from details import Details

if __name__ == '__main__':
    details = Details()
    input_name = input("Please input your player name -> ")
    details.input_valid_name(input_name)
    input_birth = input("Please input your birth date: yyyymmdd -> ")
    details.input_valid_birth(input_birth)
    
    game = LuckyGame()
    game.game_logic(details.name)