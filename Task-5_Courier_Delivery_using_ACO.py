# Task 5: Courier Delivery using ACO
import random

def aco_courier(dist, n_ants=5, iters=20, alpha=1, beta=2, evap=0.5):
    random.seed(42)
    n = len(dist)
    phero = [[1.0] * n for _ in range(n)]
    best_route, best_d = None, float('inf')
    for _ in range(iters):
        for _ in range(n_ants):
            route = [0]
            while len(route) < n:
                curr = route[-1]
                unvis = [i for i in range(n) if i not in route]
                probs = [(phero[curr][j]**alpha) * ((1.0 / dist[curr][j])**beta) for j in unvis]
                total = sum(probs)
                route.append(random.choices(unvis, weights=[p / total for p in probs])[0])
            route.append(0)
            d = sum(dist[route[i]][route[i+1]] for i in range(n))
            if d < best_d: best_route, best_d = route, d
        for i in range(n):
            for j in range(n): phero[i][j] *= (1 - evap)
        for i in range(n): phero[best_route[i]][best_route[i+1]] += 100.0 / best_d
    return best_route, best_d

places = ["Hub", "A", "B", "C", "D"]
dist = [
    [0, 12, 10, 19, 8],
    [12, 0, 3, 7, 6],
    [10, 3, 0, 4, 14],
    [19, 7, 4, 0, 9],
    [8, 6, 14, 9, 0]
]
route, cost = aco_courier(dist)
print("Optimal Courier Route:", " -> ".join(places[i] for i in route))
print("Total Distance:", cost, "km")

# Output:
# Optimal Courier Route: Hub -> A -> B -> C -> D -> Hub
# Total Distance: 36 km
