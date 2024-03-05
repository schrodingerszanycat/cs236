from math import factorial, isqrt, floor
from queue import Queue

def knuth_conjecture(target):
    queue = Queue()
    visited = set()

    # Initial state: starting with 4
    queue.put((4, "4"))
    visited.add(4)

    while not queue.empty():
        current_number, current_expression = queue.get()

        # Check if the current number is equal to the target
        if current_number == target:
            return current_expression

        try:
            # Apply factorial operation
            factorial_result = factorial(current_number)
            if factorial_result not in visited:
                queue.put((factorial_result, f"factorial {current_expression}"))
                visited.add(factorial_result)
        except OverflowError:
            # Skip factorial operation if it causes an OverflowError
            pass

        # Apply square root operation
        sqrt_result = isqrt(current_number)
        if sqrt_result not in visited:
            queue.put((sqrt_result, f"root of {current_expression}"))

        # Apply floor operation
        floor_result = floor(current_number / 2)
        if floor_result not in visited:
            queue.put((floor_result, f"floor of {current_expression}"))
            visited.add(floor_result)

    return None

# Target number is 9
target_number = 5
result = knuth_conjecture(target_number)

if result:
    print(f"Steps to reach {target_number}: {result}")
else:
    print(f"Cannot reach {target_number} using Knuth's conjecture.")
