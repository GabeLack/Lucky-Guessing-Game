import unittest

from luckygame import LuckyGame
from details import Details

class TestLuckyGame(unittest.TestCase):

    def setUp(self):
        """Set up a fresh instance of LuckyGame for each test."""
        # Instancing
        self.d = Details()
        self.d.in_name('John Doe')
        self.d.in_birth('19510101')
        self.lg = LuckyGame()

if __name__ == '__main__':
    unittest.main()
