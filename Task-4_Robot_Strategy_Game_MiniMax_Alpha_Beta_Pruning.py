# Task 4: Robot Strategy Game – Mini-Max with Alpha-Beta Pruning

def minimax(board, depth, is_max, alpha, beta):
    lines = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a, b, c in lines:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return 10 - depth if board[a] == 'O' else depth - 10
    if ' ' not in board: return 0

    if is_max:
        max_eval = -float('inf')
        for i in [i for i, v in enumerate(board) if v == ' ']:
            board[i] = 'O'
            max_eval = max(max_eval, minimax(board, depth + 1, False, alpha, beta))
            board[i] = ' '
            alpha = max(alpha, max_eval)
            if beta <= alpha: break
        return max_eval
    else:
        min_eval = float('inf')
        for i in [i for i, v in enumerate(board) if v == ' ']:
            board[i] = 'X'
            min_eval = min(min_eval, minimax(board, depth + 1, True, alpha, beta))
            board[i] = ' '
            beta = min(beta, min_eval)
            if beta <= alpha: break
        return min_eval

def best_move(board):
    moves = [i for i, v in enumerate(board) if v == ' ']
    best_idx, best_val = -1, -float('inf')
    for m in moves:
        board[m] = 'O'
        val = minimax(board, 0, False, -float('inf'), float('inf'))
        board[m] = ' '
        if val > best_val:
            best_val, best_idx = val, m
    return best_idx

# Board state: 'X' threatens row 1 (positions 0 and 2)
board = ['X', ' ', 'X', ' ', 'O', ' ', ' ', ' ', ' ']
move = best_move(board)
board[move] = 'O'
print(f"Robot ('O') Chooses Position {move}:")
for i in range(0, 9, 3): 
    print(" " + " | ".join(board[i:i+3]))

# Output:
# Robot ('O') Chooses Position 1:
#  X | O | X
#    | O |  
#    |   |  
