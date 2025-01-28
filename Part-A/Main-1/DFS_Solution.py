def water_jug_dfs(jug1_capacity,jug2_capacity, target):
    stack = [(0,0)]
    visited = set()
    path = []

    def dfs(jug1, jug2):
        # Mark the current state as visited
        visited.add((jug1, jug2))
        path.append((jug1, jug2))

        # Check if the target is achieved
        if jug1 == target or jug2 == target:
            return True

        # Generate all possible next states
        possible_moves = [
            (jug1_capacity, jug2),  # Fill jug1
            (jug1, jug2_capacity),  # Fill jug2
            (0, jug2),              # Empty jug1
            (jug1, 0),              # Empty jug2
            (max(0, jug1 - (jug2_capacity - jug2)), min(jug2_capacity, jug2 + jug1)),  # Pour jug1 into jug2
            (min(jug1_capacity, jug1 + jug2), max(0, jug2 - (jug1_capacity - jug1)))  # Pour jug2 into jug1
        ]

        for new_jug1, new_jug2 in possible_moves:
            if (new_jug1, new_jug2) not in visited:
                if dfs(new_jug1, new_jug2):
                    return True
                path.pop()  # Backtrack if the move does not lead to a solution

        return False

    # Start DFS from the initial state
    if dfs(0, 0):
        print("Solution is:")
        for state in path:
            print(f"jug-1: {state}, jug-2: {state[1]}")
    else:
        print("No solution found")

# Example usage
jug1_capacity = 4
jug2_capacity = 3
target = 2
water_jug_dfs(jug1_capacity, jug2_capacity, target)