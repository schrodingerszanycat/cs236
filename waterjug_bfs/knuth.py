# import math
# from math import factorial
# from queue import Queue

# def knuth_conjecture(n):
#     queue = Queue()
#     queue.put((4, "4"))

#     while not queue.empty():
#         current, expression = queue.get()

#         if current == n:
#             return expression

#         # Apply factorial operation
#         new_val = factorial(current)
#         new_expr = f"factorial({current})"
#         queue.put((new_val, expression + f" -> {new_expr}"))

#         # Apply square root operation
#         if current > 1:
#             new_val = int(math.sqrt(current))
#             new_expr = f"sqrt({current})"
#             queue.put((new_val, expression + f" -> {new_expr}"))

#         # Apply floor operation
#         new_val = current // 1
#         new_expr = f"floor({current})"
#         queue.put((new_val, expression + f" -> {new_expr}"))

#     return "No solution found."

# # Find the steps to reach 9
# result = knuth_conjecture(5)
# print(result)

#with custom factorial

import math
from queue import Queue

def custom_factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def knuth_conjecture(target):
    queue = Queue()
    queue.put((4, "4"))

    while not queue.empty():
        current, expression = queue.get()

        if current == target:
            return expression

        # Apply custom factorial operation
        new_val = custom_factorial(current)
        new_expr = f"custom_factorial({current})"
        queue.put((new_val, expression + f" -> {new_expr}"))

        # Apply square root operation
        if current > 1:
            new_val = int(math.sqrt(current))
            new_expr = f"sqrt({current})"
            queue.put((new_val, expression + f" -> {new_expr}"))

        # Apply floor operation
        new_val = current // 1
        new_expr = f"floor({current})"
        queue.put((new_val, expression + f" -> {new_expr}"))

    return "No solution found."

# Find the steps to reach 9
result = knuth_conjecture(5)
print(result)
