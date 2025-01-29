def tsp_solution(dist_matrix, start=0):
    n = len(dist_matrix)
    unvisited = set(range(n))
    unvisited.remove(start)
    path = [start]
    curr_city = start
    total_cost = 0
    
    while unvisited:
        next_city = min(unvisited, key = lambda city:dist_matrix[curr_city][city])
        total_cost += dist_matrix[curr_city][next_city]
        path.append(next_city)
        unvisited.remove(next_city)
        curr_city = next_city
        
    total_cost += dist_matrix[curr_city][start]
    path.append(start)
    return path, total_cost
    
        
dist_matrix = [[1,2,3,4],[2,3,4,5],[5,4,5,4],[4,5,6,7]]
start_city = 0
path, total_cost = tsp_solution(dist_matrix, start=start_city)
print(path)
print(total_cost) 