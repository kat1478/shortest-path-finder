import heapq

class Board:
    def __init__(self, board):
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])
        self.start, self.end = self.find_X_positions()
    
    def find_X_positions(self):
        positions = [(r, c) for r in range(self.rows) for c in range(self.cols) if self.board[r][c] == 'X']
        if len(positions) != 2:
            raise ValueError("Plansza musi zawierać dokładnie dwa pola z literą 'X'.")
        return positions[0], positions[1]

    def dijkstra(self):
        heap = [(0, self.start)]
        costs = {self.start: 0}
        visited = set()
        parent = {}

        while heap:
            cost, (x, y) = heapq.heappop(heap)
            if (x, y) in visited:
                continue
            visited.add((x, y))

            if (x, y) == self.end:
                return self.reconstruct_path(parent), cost

            for nx, ny in self.get_neighbors(x, y):
                new_cost = cost + self.get_cost(x, y, nx, ny)
                if (nx, ny) not in costs or new_cost < costs[(nx, ny)]:
                    costs[(nx, ny)] = new_cost
                    heapq.heappush(heap, (new_cost, (nx, ny)))
                    parent[(nx, ny)] = (x, y)
        return [], float('inf')

    def get_neighbors(self, x, y):
        neighbors = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols and self.board[nx][ny] != ' ':
                neighbors.append((nx, ny))
        return neighbors

    def get_cost(self, x, y, nx, ny):
        if self.board[x][y] == 'J' or self.board[nx][ny] == 'J':
            return 0
        if self.board[nx][ny] in ('X', 'J'):  # Sprawdzenie dla X i J
            return 0
        return int(self.board[nx][ny])



    def reconstruct_path(self, parent):
        path = set()
        current = self.end
        while current != self.start:
            path.add(current)
            current = parent[current]
        path.add(self.start)
        return path
