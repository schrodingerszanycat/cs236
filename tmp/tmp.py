# initial_state = [[3, 8, 1], [6, 2, 5], [4, 7, ' ']]
# goal_state = [[1, 2, 3], [8, 4, ' '], [7, 6, 5]]

# class QueueFrontier:

#     def __init__(self):
#         self.frontier = []

#     def add(self, state):
#         self.frontier.append(state)

#     def pop(self):
#         if self.empty():
#             raise Exception("empty frontier")
#         else:
#             node = self.frontier[0]
#             self.frontier = self.frontier[1:]
#             return node

#     def empty(self):
#         return len(self.frontier) == 0

# #def actions(state):

# def find_empty_cell():
#     for i in range(0, 3):
#         for j in range(0, 3):
#             if state[i][j] == ' ':
#                 return [i, j]
#     return [-1, -1]

# def solve_n_puzzle():
#     explored = set()
#     frontier = QueueFrontier()
#     frontier.add(initial_state)
#     while not frontier.empty():
#         state = frontier.pop()
#         if isGoal(state):
#             print_solution_path(state)
#             return
#         successor_states = actions()
#         for state in successor_states:
#             if (state in explored):
#                 continue
#             frontier.append(state)


# solve_n_puzzle()
# # print(state)
# # print(find_empty_cell())

#---------------------------------------------------------------------
# initial_state = [[3, 8, 1], [6, 2, 5], [4, 7, ' ']]
# goal_state = [[1, 2, 3], [8, 4, ' '], [7, 6, 5]]

# class Node():
#     def __init__(self, state, parent):
#         self.state = state
#         self.parent = parent
#         #self.action = action

# class QueueFrontier:

#     def __init__(self):
#         self.frontier = []

#     def add(self, node):
#         self.frontier.append(node)

#     def pop(self):
#         if self.empty():
#             raise Exception("empty frontier")
#         else:
#             node = self.frontier[0]
#             self.frontier = self.frontier[1:]
#             return node

#     def empty(self):
#         return len(self.frontier) == 0

# def actions(node):
    
#     pass

# def isGoal(node):
#     return node.state == goal_state

# def find_empty_cell(node):
#     for i in range(0, 3):
#         for j in range(0, 3):
#             if node.state[i][j] == ' ':
#                 return [i, j]
#     return [-1, -1]

# def print_solution_path(node):
    
#     pass

# def solve_n_puzzle():
#     explored = set()
#     frontier = QueueFrontier()
#     node = Node()
#     frontier.add(node(state=initial_state, parent=None))
#     while not frontier.empty():
#         node = frontier.pop()
#         if isGoal(node):
#             print_solution_path(node)
#             return
#         successor_states = actions(node)
#         for successor_state in successor_states:
#             if tuple(map(tuple, successor_state)) in explored:
#                 continue
#             frontier.add(Node(state=successor_state, parent=node))
#             explored.add(tuple(map(tuple, Node(state=successor_state, parent=node))))

# solve_n_puzzle()