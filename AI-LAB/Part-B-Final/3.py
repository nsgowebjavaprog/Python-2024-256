# 3 A* Alogrithm

from heapq import heappop, heappush


def astar(graph, start, goal):
    pq, visited = [(0, start, [])], set()
    while pq:
        cost, node, path = heappop(pq)
        if node in visited:
            continue
        path = path + [node]
        if node == goal:
            return path
        visited.add(node)
        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heappush(pq, (cost + weight, neighbor, path))
    return None

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}
start, goal = 'A', 'D'
print(astar(graph, start, goal))

# Output: ['A', 'B', 'C', 'D']