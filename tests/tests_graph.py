import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from graph import Board
from utils import load_board


class TestBoard(unittest.TestCase):
    def test_correct_path(self):
        board_data = [
            ['J', '1', '1', '2', 'J'],
            ['1', '2', 'X', '2', '1'],
            ['J', '0', '4', '1', 'J'],
            ['1', '2', 'X', '1', '1'],
            ['J', '1', '1', '1', 'J']
        ]
        board = Board(board_data)
        path, cost = board.dijkstra()
        self.assertEqual(cost, 3)  # Oczekiwany koszt
        self.assertIn((1, 2), path)
        self.assertIn((3, 2), path)
        
    def test_empty_file(self):
        with self.assertRaises(IndexError):
            board_data = load_board('tests/empty.txt')
            Board(board_data)

    def test_invalid_board(self):
        board_data = [
            ['J', '1', '1'],
            ['1', '2', '2'],
            ['J', '0', '4']
            ]
        with self.assertRaises(ValueError):  # Sprawdzamy, czy funkcja rzuca wyjątek
            Board(board_data)


if __name__ == '__main__':
    unittest.main()
