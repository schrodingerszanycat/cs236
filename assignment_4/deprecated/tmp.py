class EightQ:

    def __init__(self):
        self.size = 8

    def solve_dfs(self):
        solutions = []
        stack = [[]]
        while stack:
            solution = stack.pop()
            if self.isNotSafe(solution):
                continue
            row = len(solution)
            if row == self.size:
                solutions.append(solution)
                continue
            for col in range(self.size):
                queen = (row, col)
                queens = solution.copy()
                queens.append(queen)
                stack.append(queens)
        return solutions

    def solve_bfs(self):
        solutions = []
        queue = []
        queue.append([])

        while queue:
            solution = queue.pop(0)
            if self.isNotSafe(solution):
                continue
            row = len(solution)
            if row == self.size:
                solutions.append(solution)
                continue
            for col in range(self.size):
                queen = (row, col)
                queens = solution.copy()
                queens.append(queen)
                queue.append(queens)
        return solutions


    # def solve_iddfs(self):
    #     solutions = []
    #     for i in range(self.size):
    #         stack = [[]]
    #         while stack:
    #             solution = stack.pop()
    #             if self.isNotSafe(solution):
    #                 continue
    #             row = len(solution)
    #             if row == self.size:
    #                 solutions.append(solution)
    #                 continue
    #             for col in range(self.size):
    #                 queen = (row, col)
    #                 queens = solution.copy()
    #                 queens.append(queen)
    #                 stack.append(queens)
    #     res = []
    #     [res.append(x) for x in solutions if x not in res]
    #     return res

    def isNotSafe(self, queens):
        for i in range(1, len(queens)):
            for j in range(0, i):
                a, b = queens[i]
                c, d = queens[j]
                if a == c or b == d or abs(a - c) == abs(b - d):
                    return True
        return False

    def print(self, queens):
        for i in range(self.size):
            print(' ---' * self.size)
            for j in range(self.size):
                p = 'Q' if (i, j) in queens else ' '
                print('| %s ' % p, end='')
            print('|')
        print(' ---' * self.size)
    
    def solve_dfs_complete(self):
        solutions = []
        stack = [[]]
        while stack:
            solution = stack.pop()
            if self.isNotSafe(solution):
                continue
            row = len(solution)
            if row == self.size:
                solutions.append(solution)
                continue
            for col in range(self.size):
                queen = (row, col)
                queens = solution.copy()
                queens.append(queen)
                stack.append(queens)
        return solutions

def main():
    eight_queens = EightQ()

    # Incremental formulation
    dfs_solutions = eight_queens.solve_dfs()
    bfs_solutions = eight_queens.solve_bfs()
    #iddfs_solutions = eight_queens.solve_iddfs()

    # Complete Formulation
    #dfs_solutions_complete = eight_queens.solve_dfs_complete()

    for i, solution in enumerate(dfs_solutions):
        print('DFS Solution %d:' % (i + 1))
        eight_queens.print(solution)

    for i, solution in enumerate(bfs_solutions):
        print('BFS Solution %d:' % (i + 1))
        eight_queens.print(solution)

    # for i, solution in enumerate(iddfs_solutions):
    #     print('IDDFS Solution %d:' % (i + 1))
    #     eight_queens.print(solution)
    
    # for i, solution in enumerate(dfs_solutions_complete):
    #     print('DFS Solution %d:' % (i + 1))
    #     eight_queens.print(solution)

    print('Total DFS solutions: %d' % len(dfs_solutions))
    print('Total BFS solutions: %d' % len(bfs_solutions))
    #print('Total IDDFS solutions: %d' % len(iddfs_solutions))
    #print('Total DFS solutions using complete form.: %d' % len(dfs_solutions_complete))

if __name__ == '__main__':
    main()
