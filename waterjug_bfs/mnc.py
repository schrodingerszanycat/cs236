# at start boat is on left (1)
M = 3
C = 3
boat_capacity = 2

open_list = list()
closed_list = list()


class State:
    def __init__(self, missionaries, cannibals, boat):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat  # 1 on starting side 0 on opposite side
        self.parent = None

    def __eq__(self, other):
        return self.missionaries == other.missionaries and self.cannibals == other.cannibals and self.boat == other.boat

    def __str__(self):
        return f"M: {self.missionaries}, C: {self.cannibals}, Boat: {'left' if self.boat == 1 else 'right'}"

    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 0

    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0 or self.cannibals > C or self.missionaries > M:
            return False
        if self.missionaries != 0 and self.missionaries < self.cannibals:
            return False
        if (M - self.missionaries) != 0 and (M - self.missionaries) < (C - self.cannibals):
            return False
        return True


def generate_states(current_state: State):
    newStates = []
    if (current_state.boat == 1):
        # carrying 1 person
        newStates.append(State(current_state.missionaries - 1, current_state.cannibals, 0))
        newStates.append(State(current_state.missionaries, current_state.cannibals - 1, 0))
        # carrying 2 persons
        newStates.append(State(current_state.missionaries - 2, current_state.cannibals, 0))
        newStates.append(State(current_state.missionaries, current_state.cannibals - 2, 0))
        newStates.append(State(current_state.missionaries - 1, current_state.cannibals - 1, 0))

    if (current_state.boat == 0):
        # carrying 1 person
        newStates.append(State(current_state.missionaries + 1, current_state.cannibals, 1))
        newStates.append(State(current_state.missionaries, current_state.cannibals + 1, 1))
        # carrying 2 persons
        newStates.append(State(current_state.missionaries + 2, current_state.cannibals, 1))
        newStates.append(State(current_state.missionaries, current_state.cannibals + 2, 1))
        newStates.append(State(current_state.missionaries + 1, current_state.cannibals + 1, 1))

    return newStates

def bfs():
    initial_state = State(M, C, 1)
    if initial_state.is_goal():
        return initial_state

    open_list.append(initial_state)

    while open_list:
        current_state = open_list.pop(0)

        if current_state.is_goal():
            return current_state

        closed_list.append(current_state)

        for state in generate_states(current_state):
            if state not in closed_list and state not in open_list and state.is_valid():
                open_list.append(state)
                state.parent = current_state


solution_state = bfs()

path = []
while solution_state is not None:
    path.append(solution_state)
    solution_state = solution_state.parent

for state in reversed(path):
    print(state)