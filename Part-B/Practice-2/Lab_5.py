def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False

    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i] == j:
            return False

    for i, j in zip(range(row-1, -1, -1), range(col+1, len(board))):
        if board[i] == j:
            return False

    return True

def solve_n_queen(board, row):
    if row == len(board):
        return [board[:]]  

    solutions = []
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            solutions.extend(solve_n_queen(board, row+1))
            board[row] = -1 
    return solutions

def print_solution(solution):
    for row in solution:
        print(''.join("Q" if i==row else "--" for i in range(len(solution))))
        print()

n = 8
board = [-1]*n

solutions = solve_n_queen(board, 0)
print(f"Number of solutions: {len(solutions)}")

if solutions:
    print("Solutions: ")     
    print_solution(solutions[0])    