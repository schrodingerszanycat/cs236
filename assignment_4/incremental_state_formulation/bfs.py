""" This is a solution for the 8 Queens problem using Breadth-First Search algorithm (BFS)"""

class QueueFrontier:

    def __init__(self):
        self.frontier = []

    def add(self, state):
        self.frontier.append(state)

    def pop(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

    def empty(self):
        return len(self.frontier) == 0


class Queens:

    def __init__(self):
        self.size = 8

    def solve_bfs(self):
        solutions = []
        self.num_explored = 0 

        frontier = QueueFrontier()
        frontier.add([])
        self.explored = set()
         
        while not frontier.empty():
            solution = frontier.pop()
            if self.conflict(solution):
                self.explored.add(tuple(solution))
                self.num_explored += 1
                continue
            row = len(solution)
            if row == self.size:
                solutions.append(solution)
                continue
            for col in range(self.size):
                queen = (row, col)
                queens = solution.copy()
                queens.append(queen)
                frontier.add(queens)
        return solutions

    def conflict(self, solution):
        for i in range(1, len(solution)):
            for j in range(0, i):
                a, b = solution[i]
                x, y = solution[j]
                if a == x or b == y or abs(a-x) == abs(b-y):
                    return True
        return False

def main():
    queens = Queens()
    solutions = queens.solve_bfs()
    print("Using BFS...")
    print("No.of solutions: ", len(solutions))
    print("No.of states explored: ", queens.num_explored)
    print("No.of states in explored set: ", len(queens.explored))
    
    
if __name__ == "__main__":
    main()

