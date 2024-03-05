from collections import deque

def water_jug_bfs(m, n, d):
    visited_states = set()
    queue = deque()
    initial_state = (0, 0)
    queue.append((initial_state, []))

    while queue:
        current_state, steps = queue.popleft()
        if current_state in visited_states:
            continue

        visited_states.add(current_state)

        jug1, jug2 = current_state

        # Check if the goal is reached
        if jug1 == d or jug2 == d:
            print("Steps to measure", d, "liters of water:")
            for step in steps:
                print(step)
            return

        # Fill jug 1
        fill_jug1 = (m, jug2)
        if fill_jug1 not in visited_states:
            queue.append((fill_jug1, steps + [f"Fill jug 1"]))

        # Fill jug 2
        fill_jug2 = (jug1, n)
        if fill_jug2 not in visited_states:
            queue.append((fill_jug2, steps + [f"Fill jug 2"]))

        # Empty jug 1
        empty_jug1 = (0, jug2)
        if empty_jug1 not in visited_states:
            queue.append((empty_jug1, steps + [f"Empty jug 1"]))

        # Empty jug 2
        empty_jug2 = (jug1, 0)
        if empty_jug2 not in visited_states:
            queue.append((empty_jug2, steps + [f"Empty jug 2"]))

        # Pour water from jug 1 to jug 2
        pour_jug1_to_jug2 = (max(0, jug1 - (n - jug2)), min(jug1 + jug2, n))
        if pour_jug1_to_jug2 not in visited_states:
            queue.append((pour_jug1_to_jug2, steps + [f"Pour water from jug 1 to jug 2"]))

        # Pour water from jug 2 to jug 1
        pour_jug2_to_jug1 = (min(jug1 + jug2, m), max(0, jug2 - (m - jug1)))
        if pour_jug2_to_jug1 not in visited_states:
            queue.append((pour_jug2_to_jug1, steps + [f"Pour water from jug 2 to jug 1"]))

    print("No solution found.")

# Example with m=4, n=5, d=7
water_jug_bfs(4, 5, 7)
