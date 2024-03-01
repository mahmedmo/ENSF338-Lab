
import timeit

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


#Question 3
#For this question, we will use an ordinary binary search to search a sorted array.
#Here is an efficient binary search example.
def binary_search(sorted_array, target):
    low, high = 0, len(sorted_array) - 1

    while low <= high:
        mid = (low + high) // 2
        key = sorted_array[mid]
        if key == target:
            return mid
        elif key < target:
            low = mid + 1
        else:
            high = mid - 1  

    return -1  

sorted_array = input_array = [i for i in range(1, 1001)]

def dif_binary_search(array, target, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low <= high:
        mid = (low + high) // 2
        key = array[mid]

        if key == target:
            return mid
        elif key < target:
            return dif_binary_search(array, target, mid + 1, high)  
        else:
            return dif_binary_search(array, target, low, mid - 1)

    return -1 


def measure_execution_time(func, *args, **kwargs):
    start_time = timeit.default_timer()
    result = func(*args, **kwargs)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time
    return execution_time

# Experiment parameters
input_size = 1000


# Generate a sorted array for the experiment
input_array = [i for i in range(1, input_size + 1)]

# Measure execution time for binary_search
binary_search_times = [measure_execution_time(binary_search, input_array, np.random.randint(1, input_size + 1)) for _ in range(100)]

# Measure execution time for dif_binary_search
dif_binary_search_times = [measure_execution_time(dif_binary_search, input_array, np.random.randint(1, input_size + 1)) for _ in range(100)]

# Plotting the distribution
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))

sns.histplot(binary_search_times, bins=20, kde=True, label='binary_search')
sns.histplot(dif_binary_search_times, bins=20, kde=True, label='dif_binary_search')

plt.title('Distribution of Execution Times for Binary Search Implementations')
plt.xlabel('Execution Time (seconds)')
plt.ylabel('Frequency')
plt.legend()
plt.show() 
#Question 4
#An ordinary binary search would have a worst complexity of O(log n)
#The inefficient binary search would have a worst complexity of O(
