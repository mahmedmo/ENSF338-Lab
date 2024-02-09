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

size = 1
#randomized arrays with elements valued from 1- 100 with size 5 incremented by each subsequent array
arr_random = [[random.randint(1,100) for i in range(size + i)] for i in range(20)]
print(len(arr_random[19]))
insertion_sort_time = []
binary_insertion_sort_time = []

for x in range(20):
    #average case insertion_sort (n^2)
    insertion_sort_time.append(timeit.timeit(lambda: insertion_sort(arr_random[x])))
    print("insertion_sort: pass",x)
    #average case binary_insertion_sort (n^2)
    binary_insertion_sort_time.append(timeit.timeit(lambda: binary_insertion_sort(arr_random[x])))
    print("binary_insertion_sort: pass",x)

sizes = [1 + i for i in range(20)]  

plt.plot(sizes, insertion_sort_time, label='Insertion Sort (Average Case)', marker='o')
plt.plot(sizes, binary_insertion_sort_time, label='Binary Insertion Sort (Average Case)', marker='x')
plt.set_title('Average Case Performance')
plt.set_xlabel('Array Size')
plt.set_ylabel('Time (s)')
plt.legend()
plt.show()