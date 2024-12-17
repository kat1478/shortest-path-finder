from utils import load_board
from graph import Board
import sys

def print_board(board, path):
    for r in range(len(board)):
        for c in range(len(board[0])):
            if (r, c) in path:
                print(board[r][c], end='')
            else:
                print(' ', end='')
        print()

def main():
    if len(sys.argv) != 2:
        print("Użycie: python main.py <ścieżka_do_pliku>")
        return
    
    file_path = sys.argv[1]
    board_data = load_board(file_path)
    board = Board(board_data)

    path, cost = board.dijkstra()
    print_board(board_data, path)
    print(f"Koszt: {cost}")

if __name__ == "__main__":
    main()
