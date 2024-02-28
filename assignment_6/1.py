import numpy as np
import sys

def hill_climbing(f, lower, upper, step_size):
    if upper < lower:
        return None
    current = lower
    f_max = -sys.maxsize-1
    while current < upper:
        neighbor = current + step_size
        if f(neighbor) > f(current):
            f_max = max(f_max, f(neighbor))
        else:
            break  
        current = neighbor
    return f_max

def main():
    f_order = int(input("Enter the order of f(x): "))
    coeffs = []
    for i in range(f_order + 1):
        ele = float(input("Enter coefficients in ascending order: "))
        coeffs.append(ele)
    f = np.poly1d(coeffs)
    print("f(x) =", f)
    l = float(input("Lower bound: "))
    u = float(input("Upper bound: "))
    step = float(input("Step size: "))
    val = hill_climbing(f, l, u, step)
    print("Maximum value found:", val)
    #print(f(-2.892), f(2.077))

if __name__ == "__main__":
    main()

#-2.892, 2.077
