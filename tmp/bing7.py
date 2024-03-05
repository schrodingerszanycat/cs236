from collections import deque

def water_jug_bfs(m, n, d):
    # Initialize the queue and visited set
    queue = deque([(0, 0)])
    visited = set([(0, 0)])

    while queue:
        x, y = queue.popleft()

        # Check if we've reached the goal state
        if x == d or y == d:
            return visited

        # Explore valid next states
        next_states = [
            (m, y),  # Fill Jug 1
            (x, n),  # Fill Jug 2
            (0, y),  # Empty Jug 1
            (x, 0),  # Empty Jug 2
            (max(0, x + y - n), min(x + y, n)),  # Pour from Jug 1 to Jug 2
            (min(x + y, m), max(0, x + y - m))   # Pour from Jug 2 to Jug 1
        ]

        for next_x, next_y in next_states:
            if (next_x, next_y) not in visited:
                visited.add((next_x, next_y))
                queue.append((next_x, next_y))

    return None  # No solution found

def print_steps(visited):
    # Backtrack from the goal state to print the steps
    x, y = 0, 0
    steps = []
    while (x, y) != (4, 1):
        for dx, dy, action in [(m, 0, "Fill Jug 1"), (0, n, "Fill Jug 2"),
                               (-x, 0, "Empty Jug 1"), (0, -y, "Empty Jug 2"),
                               (min(x + y, m) - x, max(0, x + y - m), "Pour Jug 1 to Jug 2"),
                               (max(0, x + y - n), min(x + y, n) - y, "Pour Jug 2 to Jug 1")]:
            if (x + dx, y + dy) in visited:
                steps.append(action)
                x, y = x + dx, y + dy
                break

    for step in steps[::-1]:
        print(step)

if __name__ == "__main__":
    m, n, d = 4, 5, 7
    visited_states = water_jug_bfs(m, n, d)
    if visited_states:
        print("Steps to measure {} liters:".format(d))
        print_steps(visited_states)
    else:
        print("No solution found.")
