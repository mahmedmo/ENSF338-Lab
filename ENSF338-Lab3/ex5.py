import timeit
import random
import sys 
import numpy as np
import matplotlib.pyplot as plt
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def binary_search(arr, val, start, end):
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1
    if start > end:
        return start

    mid = (start + end) // 2
    if arr[mid] < val:
        return binary_search(arr, val, mid+1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid-1)
    else:
        return mid

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i-1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
    return arr

#randomized arrays with elements valued from 1- 100 i is added by 10 each iteration to the size of the array
arr_random = [[random.randint(1,100) for i in range(i*10)] for i in range(20)]

insertion_sort_time = []
binary_insertion_sort_time = []

for x in range(20):
    #average case insertion_sort (n^2)
    insertion_sort_time.append(timeit.timeit(lambda: insertion_sort(arr_random[x]), number=1))
    print("insertion_sort: pass",x+1)
    #average case binary_insertion_sort (n^2)
    binary_insertion_sort_time.append(timeit.timeit(lambda: binary_insertion_sort(arr_random[x]),number=1))
    print("binary_insertion_sort: pass",x+1)

sizes = [(i*10)for i in range(20)]  

#Insertion vs. Binary Insertion Plot
plt.plot(sizes, insertion_sort_time, label='Insertion Sort (Average Case)', marker='o')
plt.plot(sizes, binary_insertion_sort_time, label='Binary Insertion Sort (Average Case)', marker='x')
plt.xlabel('Array Size')
plt.ylabel('Time (s)')
plt.legend()
plt.show()

#Question 4
# The Binary Insertion sort and the traditional insertion sort algorithms are both the same complexity of O(n^2). 
# However, despite this the binary insertion sort performs faster at greater array sizes. 
# This occurs due to the faster algorithmic advantage Binary Insertion sort has in comparisons. 
# It can search and find the value much more efficiently thanks to its use of binary search opposed to insertion sort’s linear search. 
# However, this does not change its complexity as it still needs to complete the same number of swaps, 
# the only benefit is its ability to find the value that must be swapped (or need to swap) faster.