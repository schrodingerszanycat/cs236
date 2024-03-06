import copy
import heapq

initial_state = [[8, 2, ' '], [3, 4, 7], [5, 1, 6]]
#goal_state = [[3, 8, 2], [' ', 4, 7], [5, 1, 6]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, ' ']]

class IDSNode:
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

class AStarNode():
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g  
        self.h = h  

    def __lt__(self, other):
        return self.f() < other.f()

    def f(self):
        return self.g + self.h

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.size = 0

    def add(self, node):
        heapq.heappush(self.heap, (node.f(), node))
        self.size = max(self.size, len(self.heap))

    def pop(self):
        if self.empty():
            raise Exception("Empty frontier")
        else:
            _, node = heapq.heappop(self.heap)
            return node

    def empty(self):
        return len(self.heap) == 0
    
    def max_queue_size(self):
        return self.size

def misplaced_tiles_heuristic(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j]:
                count += 1
    return count

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

def print_solution_path(node, search):
    path = []
    while node:
        path.insert(0, node.state)
        node = node.parent

    print(len(path), "is the length of the solution path.")
    if search == 1:
        print("Here is the solution path:\n")
        for state in path:
            for row in state:
                print(row)
            print()
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
            print_solution_path(current_node, 0)
            return True

        if depth_limit > 0:
            successor_states = actions(current_node)
            num_generated += len(successor_states)

            for successor_state in successor_states:
                if tuple(map(tuple, successor_state)) in explored:
                    continue
                frontier.add(IDSNode(state=successor_state, parent=current_node))
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

def A_star_search(initial_node):
    explored = set()
    num_explored = 0
    num_generated = 0
    frontier = PriorityQueue()
    frontier.add(initial_node)

    while not frontier.empty():
        current_node = frontier.pop()

        if is_goal(current_node, goal_state):
            print(num_explored, "states explored.")
            print(num_generated, "states generated.")
            print(frontier.max_queue_size(), "is the maximum length of the queue structure.")
            print_solution_path(current_node, 1)
            return

        if tuple(map(tuple, current_node.state)) not in explored:
            explored.add(tuple(map(tuple, current_node.state)))
            num_explored += 1

            successor_states = actions(current_node)
            num_generated += len(successor_states)

            for successor_state in successor_states:
                g = current_node.g + 1
                h = misplaced_tiles_heuristic(successor_state)
                frontier.add(AStarNode(state=successor_state, parent=current_node, g=g, h=h))

    print("Goal not found.")

def solve_n_puzzle_A_star():
    print("Calculating...")
    initial_node = AStarNode(state=initial_state)
    A_star_search(initial_node)

def solve_n_puzzle():
    print("Calculating...")
    initial_node = IDSNode(state=initial_state)
    iterative_deepening_search(initial_node)

print("Using IDS:")
solve_n_puzzle()
print("Using A star search:")
solve_n_puzzle_A_star()