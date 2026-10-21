# Task 2: CPU Task Scheduling – Hill Climbing
import random

def hill_climbing(tasks, cpus=3, iters=50):
    sched = [[] for _ in range(cpus)]
    for t in tasks: sched[random.randint(0, cpus - 1)].append(t)
    cost = lambda s: max(sum(tasks[t] for t in c) for c in s)
    
    for _ in range(iters):
        loads = [sum(tasks[t] for t in c) for c in sched]
        h = loads.index(max(loads))
        best_s, best_c = sched, cost(sched)
        for t in sched[h]:
            for target in range(cpus):
                if target != h:
                    nbr = [list(c) for c in sched]
                    nbr[h].remove(t); nbr[target].append(t)
                    if cost(nbr) < best_c:
                        best_s, best_c = nbr, cost(nbr)
        if best_c < cost(sched): sched = best_s
        else: break
    return sched, cost(sched)

tasks = {'T1': 30, 'T2': 50, 'T3': 10, 'T4': 40, 'T5': 20, 'T6': 60, 'T7': 15, 'T8': 25}
random.seed(42)
sched, makespan = hill_climbing(tasks)
print(f"Optimal Makespan: {makespan} ms")
for i, c in enumerate(sched, 1):
    print(f"CPU {i}: {c} (Load: {sum(tasks[t] for t in c)} ms)")

# Output:
# Optimal Makespan: 85 ms
# CPU 1: ['T2', 'T3', 'T8'] (Load: 85 ms)
# CPU 2: ['T5', 'T6'] (Load: 80 ms)
# CPU 3: ['T1', 'T4', 'T7'] (Load: 85 ms)
