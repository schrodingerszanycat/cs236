import numpy as np
from numpy import random
import datetime

#https://stackoverflow.com/questions/26923466/matrix-of-mean-0-and-standard-deviation-0-1-with-python
#https://stackoverflow.com/questions/33273512/random-samples-from-a-uniform-distribution-over-0-1

def main():
    m, n = 3, 3 # should be a square matrix (m == n)
    p, q = 3, 3 # all dimensions must be equal because we have to multiply their tranpose too
    A = random.normal(0, 1, (m, n))
    B = np.random.uniform(0.0, 1.0, (p, q))
    print("Matrix A")
    print(A)
    print("Matrix B")
    print(B) 

    inv_A = np.linalg.inv(A)
    print("Matrix inv_A")
    print(inv_A)
    
    t1 = datetime.datetime.now()
    print("\nMatrix A'B")
    print(np.dot(inv_A, B))
    t2 = datetime.datetime.now()
    print(f"Time taken (a): {(t2 - t1).microseconds} ms\n")

    transpose_A = np.transpose(A)
    transpose_B = np.transpose(B)
    print("Matrix A transpose")
    print(transpose_A)
    print("Matrix B transpose")
    print(transpose_B)

    t1 = datetime.datetime.now()
    print("\nMatrix A transpose into B transpose")
    print(np.dot(transpose_A, transpose_B))
    t2 = datetime.datetime.now()
    print(f"Time taken (b): {(t2 - t1).microseconds} ms\n")

if __name__ == "__main__":
    main()
