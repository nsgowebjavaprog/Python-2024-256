from collections import deque
class Puzzle8BFS:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.visited = set()

    def get_neighbors(self, state):
        grid = [list(state[i:i + 3]) for i in range(0, 9, 3)]
        zero_index = state.index('0')
        zero_row, zero_col = zero_index // 3, zero_index % 3
        
        moves = {
            "up": (-1, 0),
            "down": (1, 0),
            "left": (0, -1),
            "right": (0, 1),
        }
        neighbors = []
        
        for direction, (dr, dc) in moves.items():
            new_row, new_col = zero_row + dr, zero_col + dc
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_grid = [row[:] for row in grid]
                new_grid[zero_row][zero_col], new_grid[new_row][new_col] = new_grid[new_row][new_col], new_grid[zero_row][zero_col]
                new_state = ''.join(sum(new_grid, []))
                neighbors.append((new_state, direction))
        return neighbors

    def bfs(self):
        queue = deque([(self.start, [])])
        self.visited.add(self.start)
        while queue:
            current_state, path = queue.popleft()
            if current_state == self.goal:
                return path
            for neighbor, direction in self.get_neighbors(current_state):
                if neighbor not in self.visited:
                    self.visited.add(neighbor)
                    queue.append((neighbor, path + [direction]))
        return None

start_state = "123405678"
goal_state = "123456780"
puzzle = Puzzle8BFS(start_state, goal_state)
solution = puzzle.bfs()

if solution:
    print("Solution found with BFS:")
    for step, move in enumerate(solution, 1):
        print(f"Step {step}: Move {move}")
else:
    print("No solution found.")