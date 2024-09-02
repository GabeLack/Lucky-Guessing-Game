from luckygame import LuckyGame
from details import Details

if __name__ == '__main__':
    details = Details()
    details.input_valid_name()
    details.input_valid_birth()
    
    game = LuckyGame()
    game.game_logic(details.name)