import timeit
import matplotlib.pyplot as plt
import numpy as np

# Question 3
# For this question, we will use linear search (as inefficient implementation) and binary search (as efficient implementation) to search a sorted array.

# Implementation of linear search, which will be our inefficient implementation.
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        
    return -1


# Implementation of binary search, which will be our efficient implementation.
def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        key = arr[mid]
        if key == target:
            return mid
        elif key < target:
            low = mid + 1
        else:
            high = mid - 1  

    return -1  


# Question 4
# The worst-case complexity for linear search is O(n), when the target is 1000, the last element in the array.
# The worst-case complexity for binary search is O(logn), when the target is 500, where it must do the maximum number of divisions to reach the target.


# Question 5
arr = [i for i in range(0, 1001)] # sorted input of 1000 elements
linearsrch_times = []   # empty array for linear search times
binarysrch_times = []   # empty array for binary search times

for x in range(1000):  # runs 1000 times
    target = np.random.randint(0, 1000)    # selects random target from 1000 elements

    linearsrch_time = timeit.timeit(lambda: linear_search(arr, target), number = 1) # times linear search
    linearsrch_times.append(linearsrch_time)
    
    binarysrch_time = timeit.timeit(lambda: binary_search(arr, target), number = 1) # times binary search
    binarysrch_times.append(binarysrch_time)


# plots the times and frequencies
ax = plt.axes()
ax.set_facecolor("gainsboro")
plt.hist(linearsrch_times, bins=20, color="red", edgecolor="white", alpha=0.5, label='Inefficient (Linear Search)')
plt.hist(binarysrch_times, bins=20, color="royalblue", edgecolor="black", alpha=0.5, label='Efficient (Binary Search)')
plt.xlabel('Times')
plt.ylabel('Frequency')
plt.title('Execution Time Distribution')
plt.legend()
plt.show()
