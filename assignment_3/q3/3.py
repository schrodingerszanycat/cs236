import numpy as np

def calculate_statistics(data):
    stats = {
        'Median': np.median(data),
        'Minimum': np.min(data),
        'Maximum': np.max(data)
    }
    return stats

def multiply_matrices(matrix1, matrix2):
    product = np.dot(matrix1, matrix2)
    return product

def filter_odd_numbers(arr):
    odd_numbers = arr[arr % 2 != 0]
    return odd_numbers

def clean_dataset(dataset):
    for i in range(len(dataset)):
        dataset[i] = dataset[i].strip("\n")

def main():
    # (a. i)
    filepath = "data1.txt"
    with open(filepath, 'r') as file:
        sets = file.readlines()

    dataset = np.array([])
    for i in range(0, len(sets)):
        dataset = np.append(dataset, sets[i])

    clean_dataset(dataset)
    print(dataset)

    # (a. ii, iii, iv)
    result_arr = np.array([])
    for i in range(len(dataset)):
        set = [int(num) for num in dataset[0].split(',')]
        # print(set)
        mean = np.mean(set)
        std = np.std(set, dtype = np.float32)
        print("mean of set", i+1, ":", mean)
        print("std of set", i+1, ":", std)
        print("\n")
        lst = []
        lst.append(mean)
        lst.append(std)
        result_arr = np.append(result_arr, lst)
    
    print(result_arr)
    file = open("results.txt", "w+")
    for i in range(len(result_arr)):
        file.write(str(result_arr[i]))
        file.write(",")
        file.write("\n")
    
    print("\n")

    # (b) Calculate Statistics
    data = np.array([1, 5, 3, 7, 9, 2, 4, 6, 8, 10])
    stats = calculate_statistics(data)
    print("Statistics:", stats)

    # (c) Multiply Matrices
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    product = multiply_matrices(matrix1, matrix2)
    print("Matrix Product:\n", product)

    # (d) Filter Odd Numbers
    random_array = np.random.randint(1, 101, 10)
    filtered_odd_numbers = filter_odd_numbers(random_array)
    print("Original Array:", random_array)
    print("Filtered Odd Numbers:", filtered_odd_numbers)

if __name__ == '__main__':
    main()

