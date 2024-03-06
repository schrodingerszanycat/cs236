import copy
import heapq

initial_state = [[8, 2, ' '], [3, 4, 7], [5, 1, 6]]
#goal_state = [[3, 8, 2], [' ', 4, 7], [5, 1, 6]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, ' ']]

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

def is_goal(node):
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

def A_star_search(initial_node):
    explored = set()
    num_explored = 0
    num_generated = 0
    frontier = PriorityQueue()
    frontier.add(initial_node)

    while not frontier.empty():
        current_node = frontier.pop()

        if is_goal(current_node):
            print(num_explored, "states explored.")
            print(num_generated, "states generated.")
            print(frontier.max_queue_size(), "is the maximum length of the queue structure.")
            print_solution_path(current_node)
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

solve_n_puzzle_A_star()
