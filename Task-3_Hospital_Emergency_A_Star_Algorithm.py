# Task 3: Hospital Emergency – A* Algorithm
import heapq

def a_star(grid, start, goal):
    h = lambda p: abs(p[0] - goal[0]) + abs(p[1] - goal[1])
    pq = [(h(start), 0, start, [start])]
    visited = {}
    while pq:
        f, g, curr, path = heapq.heappop(pq)
        if curr == goal: return path, g
        if curr in visited and visited[curr] <= g: continue
        visited[curr] = g
        r, c = curr
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 0:
                heapq.heappush(pq, (g + 1 + h((nr, nc)), g + 1, (nr, nc), path + [(nr, nc)]))

# 0: Open corridor, 1: Obstacle
grid = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0]
]
path, cost = a_star(grid, (0, 0), (4, 4))
print(f"Emergency Route Cost: {cost}")
print(f"Optimal Route Path: {path}")

# Output:
# Emergency Route Cost: 8
# Optimal Route Path: [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4)]
