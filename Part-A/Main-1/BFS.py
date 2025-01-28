from collections import deque 
class Puzzle8BFS: 
    def __init__(self, start, goal): 
        self.start = start 
        self.goal = goal 
        self.visited = set()  # Track visited states to avoid redundant work 
 
    def get_neighbors(self, state): 
        """Generate all possible moves from the current state.""" 
        neighbors = [] 
        grid = [list(state[i:i + 3]) for i in range(0, 9, 3)] 
        zero_index = state.index('0')  # Find the empty space 
        zero_row, zero_col = zero_index // 3, zero_index % 3 
 
        # Possible moves with directions 
        moves = { 
            "up": (-1, 0), 
            "down": (1, 0), 
            "left": (0, -1), 
            "right": (0, 1), 
        } 
 
        for direction, (dr, dc) in moves.items(): 
            new_row, new_col = zero_row + dr, zero_col + dc 
            if 0 <= new_row < 3 and 0 <= new_col < 3: 
                # Perform the move 
                new_grid = [row[:] for row in grid] 
                new_grid[zero_row][zero_col], new_grid[new_row][new_col] = ( 
                    new_grid[new_row][new_col], 
                    new_grid[zero_row][zero_col], 
                ) 
                # Convert back to single string 
                new_state = ''.join(sum(new_grid, [])) 
                neighbors.append((new_state, direction)) 
 
        return neighbors 
 
    def bfs(self): 
        queue = deque([(self.start, [])])  # (current state, path of moves) 
        self.visited.add(self.start) 
 
        while queue: 
            current_state, path = queue.popleft() 
 
            # Check if we have reached the goal 
            if current_state == self.goal: 
                return path 
 
            # Explore neighbors 
            for neighbor, direction in self.get_neighbors(current_state): 
                if neighbor not in self.visited: 
                    self.visited.add(neighbor) 
                    queue.append((neighbor, path + [direction])) 
 
        return None  # Return None if no solution exists 
 
# Define the start and goal states as strings 
start_state = "123405678"  # '0' represents the empty space 
goal_state = "123456780" 
 
# Solve the puzzle 
puzzle = Puzzle8BFS(start_state, goal_state) 
solution = puzzle.bfs() 
 
# Print the solution 
if solution is not None: 
    print("Solution found with BFS:") 
    for step, move in enumerate(solution, 1): 
        print(f"Step {step}: Move {move}") 
else: 
    print("No solution found.")