import copy

initial_state = [[8, 2, ' '], [3, 4, 7], [5, 1, 6]]
goal_state = [[3, 8, 2], [' ', 4, 7], [5, 1, 6]]

class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

class StackFrontier:
    def __init__(self):
        self.frontier = []
        self.size = 0

    def add(self, node):
        self.frontier.append(node)
        self.size = max(self.size, len(self.frontier))

    def pop(self):
        if self.empty():
            raise Exception("Empty frontier")
        else:
            node = self.frontier.pop()
            return node

    def empty(self):
        return len(self.frontier) == 0

    def max_queue_size(self):
        return self.size

def actions(node):
    empty_cell = find_empty_cell(node)
    i, j = empty_cell
    successors = []

    # Move up
    if i > 0:
        successor_state = create_successor_state(node, i, j, i - 1, j)
        successors.append(successor_state)

    # Move down
    if i < 2:
        successor_state = create_successor_state(node, i, j, i + 1, j)
        successors.append(successor_state)

    # Move left
    if j > 0:
        successor_state = create_successor_state(node, i, j, i, j - 1)
        successors.append(successor_state)

    # Move right
    if j < 2:
        successor_state = create_successor_state(node, i, j, i, j + 1)
        successors.append(successor_state)

    return successors

def create_successor_state(node, i, j, new_i, new_j):
    successor_state = copy.deepcopy(node.state)
    successor_state[i][j], successor_state[new_i][new_j] = successor_state[new_i][new_j], successor_state[i][j]
    return successor_state

def is_goal(node, goal_state):
    return node.state == goal_state

def find_empty_cell(node):
    for i, row in enumerate(node.state):
        for j, cell in enumerate(row):
            if cell == ' ':
                return i, j
    return -1, -1

def print_solution_path(node):
    path = []
    while node:
        path.insert(0, node.state)
        node = node.parent

    print("Here is the solution path:\n")
    for state in path:
        for row in state:
            print(row)
        print()

    print(len(path), "is the length of the solution path.")
    print("Goal reached!")

def depth_limited_search(node, depth_limit, explored):
    if depth_limit < 0:
        return False

    frontier = StackFrontier()
    frontier.add(node)
    num_explored = 0
    num_generated = 0

    while not frontier.empty():
        current_node = frontier.pop()

        if is_goal(current_node, goal_state):
            print(num_explored, "states explored.")
            print(num_generated, "states generated.")
            print(frontier.max_queue_size(), "is the maximum length of the queue structure.")
            print_solution_path(current_node)
            return True

        if depth_limit > 0:
            successor_states = actions(current_node)
            num_generated += len(successor_states)

            for successor_state in successor_states:
                if tuple(map(tuple, successor_state)) not in explored:
                    frontier.add(Node(state=successor_state, parent=current_node))
                    explored.add(tuple(map(tuple, successor_state)))
                    num_explored += 1

    return False

def iterative_deepening_search(node):
    depth_limit = 0
    explored = set()

    while True:
        print(f"Trying depth limit: {depth_limit}")
        result = depth_limited_search(node, depth_limit, explored)

        if result:
            return

        depth_limit += 1

        if depth_limit > 100:
            print("Maximum depth limit reached. Exiting...")
            break

    print("Goal not found within depth limit.")

def solve_n_puzzle():
    print("Calculating...")
    initial_node = Node(state=initial_state)
    iterative_deepening_search(initial_node)

solve_n_puzzle()