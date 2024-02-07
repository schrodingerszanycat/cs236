import copy

initial_state = [[3, 8, 1], [6, 2, 5], [4, 7, ' ']]
goal_state = [[1, 2, 3], [8, 4, ' '], [7, 6, 5]]

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

def isGoal(node):
    return node.state == goal_state

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

    for state in path:
        print(state)
    print("Goal reached!")

def solve_n_puzzle():
    explored = set()
    frontier = QueueFrontier()
    initial_node = Node(state=initial_state, parent=None)
    frontier.add(initial_node)
    while not frontier.empty():
        node = frontier.pop()
        if isGoal(node):
            print_solution_path(node)
            return
        successor_states = actions(node)
        for successor_state in successor_states:
            if tuple(map(tuple, successor_state)) in explored:
                continue
            frontier.add(Node(state=successor_state, parent=node))
            explored.add(tuple(map(tuple, successor_state)))

solve_n_puzzle()

