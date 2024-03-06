import copy
import heapq

initial_state = [[8, 2, ' '], [3, 4, 7], [5, 1, 6]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, ' ']]
#goal_state = [[3, 8, 2], [' ', 4, 7], [5, 1, 6]]

class Node():
    def __init__(self, state, parent, g, h):
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

    def add(self, node):
        heapq.heappush(self.heap, (node.f(), node))

    def pop(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            _, node = heapq.heappop(self.heap)
            return node

    def empty(self):
        return len(self.heap) == 0

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

    print("Here is the solution path: \n")
    for state in path:
        for i in range(len(state)):
            print(state[i])
        print()
    print("Goal reached!")

def A_star_search(initial_node):
    explored = set()
    num_explored = 0
    frontier = PriorityQueue()
    frontier.add(initial_node)

    while not frontier.empty():
        current_node = frontier.pop()

        if isGoal(current_node):
            print(num_explored, "states explored.")
            print_solution_path(current_node)
            return

        if tuple(map(tuple, current_node.state)) not in explored:
            explored.add(tuple(map(tuple, current_node.state)))
            num_explored += 1

            successor_states = actions(current_node)
            for successor_state in successor_states:
                g = current_node.g + 1  
                h = misplaced_tiles_heuristic(successor_state)
                frontier.add(Node(state=successor_state, parent=current_node, g=g, h=h))

    print("Goal not found.")

def solve_n_puzzle_A_star():
    print("Calculating...")
    initial_node = Node(state=initial_state, parent=None, g=0, h=misplaced_tiles_heuristic(initial_state))
    A_star_search(initial_node)

solve_n_puzzle_A_star()
