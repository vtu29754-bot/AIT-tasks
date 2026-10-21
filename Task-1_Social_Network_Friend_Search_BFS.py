# Task 1: Social Network Friend Search – BFS
from collections import deque

def bfs(graph, start, target):
    q, visited = deque([[start]]), {start}
    while q:
        path = q.popleft()
        if path[-1] == target:
            return path
        for nbr in graph.get(path[-1], []):
            if nbr not in visited:
                visited.add(nbr)
                q.append(path + [nbr])
    return None

network = {
    'Alice': ['Bob', 'Charlie'],
    'Bob': ['Alice', 'David', 'Emma'],
    'Charlie': ['Alice', 'Frank'],
    'David': ['Bob'],
    'Emma': ['Bob', 'Grace'],
    'Frank': ['Charlie'],
    'Grace': ['Emma', 'Henry'],
    'Henry': ['Grace']
}

path = bfs(network, 'Alice', 'Henry')
print("Shortest Connection:", " -> ".join(path))
print("Degrees of Separation:", len(path) - 1)

# Output:
# Shortest Connection: Alice -> Bob -> Emma -> Grace -> Henry
# Degrees of Separation: 4
