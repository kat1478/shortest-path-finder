def load_board(file_path):
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]
