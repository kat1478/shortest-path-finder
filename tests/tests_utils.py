import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import load_board


class TestUtils(unittest.TestCase):
    def test_load_board(self):
        board = load_board('tests/plansza_testowa.txt')
        self.assertEqual(len(board), 5)  # Plansza ma 5 wierszy
        self.assertEqual(board[0][0], 'J')  # Pierwszy znak to 'J'

if __name__ == '__main__':
    unittest.main()
