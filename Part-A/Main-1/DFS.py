def water_jug_dfs(jug1_capacity,jug2_capacity, target):
    stack = [(0,0)]
    visited = set()
    path = []
    
    def dfs(jug1, jug2):
        if jug1 == target or jug2 == target:
            path.append((jug1, jug2))
            return True
        
        visited.app((jug1, jug2))
        path.append((jug1, jug2))
        
    possible_moves = [
        (jug1_capacity, jug2),
        (jug1, jug2_capacity),
        (0, jug2),
        (jug1, 0),
        (max(0, jug1 - (jug2_capacity - jug2)), min(jug2_capacity, jug2+jug1)),
        (min(jug1_capacity, jug1+jug2), max(0, jug2 - (jug1_capacity-jug1)))
    ]
        
    for new_jug1, new_jug2 in possible_moves:
        if(new_jug1, new_jug2) not in visited:
            if dfs(new_jug1, new_jug2):
                return True
            path.pop()
            return False
            
        dfs(0,0)
        if path and (path[-1][0] == target or path[-1][1] == target):
            print("Solution is :")
            for state in path:
                print(f"jug-1: {state[0]}, jug-2:{state[1]}")
                
        else:
            print("No-Solution")
jug1_capacity = 4
jug2_capacity = 3
target = 2
water_jug_dfs(jug1_capacity, jug2_capacity, target)                    