# https://www.eecis.udel.edu/~mccoy/courses/cisc4-681.10f/lec-materials/Chapt-6-Constraint-Satisfaction.pdf


def is_valid(row: int, col: int) -> bool:
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True


def backtrack(row: int) -> None:
    if row == 8:
        result.append([[1 if i == col else 0 for i in range(8)] for col in board])
        return
    for col in range(8):
        if is_valid(row, col):
            board[row] = col
            backtrack(row + 1)
            board[row] = -1


board = [-1] * 8
result = []
backtrack(0)
for matrix in result:
    for r in matrix:
        print(r)
    print()