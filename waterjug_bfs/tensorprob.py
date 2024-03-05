import numpy as np
import time

# Define the dimensions of the tensors
m1, n1, r1 = 3, 4, 5
m2, n2, r2 = 3, 4, 5

# Create tensors with random values
t1 = np.random.normal(0, 1, (m1, n1, r1))
t2 = np.random.rand(m2, n2, r2)

# Define the scalar coefficients
c1, c2, c3 = 2, 3, 4

# Perform the linear combination
start_time = time.time()
result_tensor = c1 * t1 + c2 * t2 + c3
end_time = time.time()

# Print the resulting tensor and the time taken
print("Resulting Tensor:")
print(result_tensor)
print("\nTime taken for linear operation: {:.6f} seconds".format(end_time - start_time))
