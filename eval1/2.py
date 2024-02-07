import copy
import numpy as np

initial_state = [[3, 8, 1], [6, 2, 5], [4, 7, ' ']]
goal_state = [[1, 2, 3], [8, 4, ' '], [7, 6, 5]]  #not reachable
#goal_state = [[3, 8, 1], [4, 6, 2], [' ', 7, 5]] #reachable

# initial_state = [[' ', 1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22, 23], [24, 25, 26, 27, 28, 29, 30, 31], [32, 33, 34, 35, 36, 37, 38, 39], [40, 41, 42, 43, 44, 45, 46, 47], [48, 49, 50, 51, 52, 53, 54, 55], [56, 57, 58, 59, 60, 61, 62, 63]]
# goal_state = np.transpose(initial_state)
# goal_state = [[16, 1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14, 15], [' ', 17, 18, 19, 20, 21, 22, 23], [24, 25, 26, 27, 28, 29, 30, 31], [32, 33, 34, 35, 36, 37, 38, 39], [40, 41, 42, 43, 44, 45, 46, 47], [48, 49, 50, 51, 52, 53, 54, 55], [56, 57, 58, 59, 60, 61, 62, 63]]

class Node():
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent

class QueueFrontier:

    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def pop(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

    def empty(self):
        return len(self.frontier) == 0

def actions(node):
    empty_cell = find_empty_cell(node)
    i, j = empty_cell
    successors = []

    # Move up
    if i > 0:
        successor_state = copy.deepcopy(node.state)
        successor_state[i][j], successor_state[i - 1][j] = successor_state[i - 1][j], successor_state[i][j]
        successors.append(successor_state)

    # Move down
    if i < 2:
        successor_state = copy.deepcopy(node.state)
        successor_state[i][j], successor_state[i + 1][j] = successor_state[i + 1][j], successor_state[i][j]
        successors.append(successor_state)

    # Move left
    if j > 0:
        successor_state = copy.deepcopy(node.state)
        successor_state[i][j], successor_state[i][j - 1] = successor_state[i][j - 1], successor_state[i][j]
        successors.append(successor_state)

    # Move right
    if j < 2:
        successor_state = copy.deepcopy(node.state)
        successor_state[i][j], successor_state[i][j + 1] = successor_state[i][j + 1], successor_state[i][j]
        successors.append(successor_state)

    return successors

# def isGoal(node):
#     return node.state == goal_state
def isGoal(node):
    return np.array_equal(node.state, goal_state)


def find_empty_cell(node):
    for i in range(0, 3):
        for j in range(0, 3):
            if node.state[i][j] == ' ':
                return [i, j]
    return [-1, -1]

def print_solution_path(node):
    path = []
    while node:
        path.insert(0, node.state)
        node = node.parent

    print("Here is the solution path: \n")
    for state in path:
        for i in range(len(state)):
            print(state[i])
        print()
    print("Goal reached!")

def solve_n_puzzle():
    print("Calculating...")
    explored = set()
    num_explored = 0
    frontier = QueueFrontier()
    initial_node = Node(state=initial_state, parent=None)
    frontier.add(initial_node)
    while not frontier.empty():
        node = frontier.pop()
        if isGoal(node):
            print(num_explored, "states explored.")
            print_solution_path(node)
            return
        successor_states = actions(node)
        for successor_state in successor_states:
            if tuple(map(tuple, successor_state)) in explored:
                continue
            frontier.add(Node(state=successor_state, parent=node))
            explored.add(tuple(map(tuple, successor_state)))
            num_explored += 1
    print(num_explored, "states explored but goal not found.")
    print("Conclusion: Goal state found not reachable from initial state.")
    print("\nNote: Change the goal state to a reachable one to view its solution path.")
    print("Exiting...")

solve_n_puzzle()

