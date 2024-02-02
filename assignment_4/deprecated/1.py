from queue import Queue

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
        queue = Queue()
        queue.put([])
        while not queue.empty():
            solution = queue.get()
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
                queue.put(queens)
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

def main():
    eight_queens = EightQ()

    dfs_solutions = eight_queens.solve_dfs()
    bfs_solutions = eight_queens.solve_bfs()
    iddfs_solutions = eight_queens.solve_iddfs()

    for i, solution in enumerate(dfs_solutions):
        print('DFS Solution %d:' % (i + 1))
        eight_queens.print(solution)

    for i, solution in enumerate(bfs_solutions):
        print('BFS Solution %d:' % (i + 1))
        eight_queens.print(solution)

    for i, solution in enumerate(iddfs_solutions):
        print('IDDFS Solution %d:' % (i + 1))
        eight_queens.print(solution)

    print('Total DFS solutions: %d' % len(dfs_solutions))
    print('Total BFS solutions: %d' % len(bfs_solutions))
    print('Total IDDFS solutions: %d' % len(iddfs_solutions))

if __name__ == '__main__':
    main()
