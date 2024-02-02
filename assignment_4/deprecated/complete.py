class EightQueensDFS:

    def __init__(self, size=8):
        self.size = size
        self.solutions = []

    def solve_dfs(self):
        self.dfs([], 0)
        return self.solutions

    def dfs(self, queens, row):
        if row == self.size:
            self.solutions.append(queens.copy())
            return

        for col in range(self.size):
            if not self.is_attacked(queens, row, col):
                queens.append((row, col))
                self.dfs(queens, row + 1)
                queens.pop()

    def is_attacked(self, queens, row, col):
        for queen_row, queen_col in queens:
            if queen_col == col or \
               queen_row + queen_col == row + col or \
               queen_row - queen_col == row - col:
                return True
        return False

    def print_solution(self, solution):
        for i in range(self.size):
            print(' ---' * self.size)
            for j in range(self.size):
                p = 'Q' if (i, j) in solution else ' '
                print('| %s ' % p, end='')
            print('|')
        print(' ---' * self.size)
        print()

def main():
    eight_queens_dfs = EightQueensDFS()
    dfs_solutions = eight_queens_dfs.solve_dfs()

    for i, solution in enumerate(dfs_solutions):
        print('DFS Solution %d:' % (i + 1))
        eight_queens_dfs.print_solution(solution)

    print('Total DFS solutions: %d' % len(dfs_solutions))

if __name__ == '__main__':
    main()
