# Task 8: 4-Queens Problem using Python

def solve_4_queens(n=4):
    def solve(row, cols, diag1, diag2, board):
        if row == n:
            solutions.append(board)
            return
        for col in range(n):
            if col not in cols and (row - col) not in diag1 and (row + col) not in diag2:
                solve(row + 1, cols | {col}, diag1 | {row - col}, diag2 | {row + col}, board + [col])
    solutions = []
    solve(0, set(), set(), set(), [])
    return solutions

for idx, sol in enumerate(solve_4_queens(), 1):
    print(f"Solution {idx}: {sol}")
    for col in sol:
        print(" ".join("Q" if i == col else "." for i in range(4)))
    print()

# Output:
# Solution 1: [1, 3, 0, 2]
# . Q . .
# . . . Q
# Q . . .
# . . Q .
# 
# Solution 2: [2, 0, 3, 1]
# . . Q .
# Q . . .
# . . . Q
# . Q . .
