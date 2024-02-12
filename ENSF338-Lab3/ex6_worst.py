import sys
sys.setrecursionlimit(100000)
import random
import timeit
import matplotlib.pyplot as plt
import numpy as np


# 6.5.1
def linear_srch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right


def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index)
        quicksort(arr, pivot_index + 1, high)


def bsrch(arr, first, last, target):
    if first <= last:
        mid = (first + last)//2
        if (target == arr[mid]):
            return mid
        elif arr[mid]< target:
            return bsrch(arr, mid + 1, last, target)
        elif arr[mid]> target:
            return bsrch(arr, first, mid-1, target)
    return -1




# 6.5.2

task = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

target = 5
elapsed_time_lin = []
elapsed_time_qb = []
for i in range(100):
    # alg 1
    elapsed_time_lin.append(timeit.timeit(lambda : linear_srch(task, target), number = 200))        # finds target 200x

    # alg 2
    current_time_qb = timeit.timeit(lambda : quicksort(task, 0, len(task)-1), number = 1)   # first sorts using quicksort
    current_time_qb += timeit.timeit(lambda : bsrch(task, 0, len(task)-1, target), number = 200)    # finds target 200x
    elapsed_time_qb.append(current_time_qb)

print(f"The average time for linear search: {sum(elapsed_time_lin)/100}")
print(f"The average time for quicksort + binary search: {sum(elapsed_time_qb)/100}\n")




# 6.5.3

sizes = [10, 20, 50, 100, 200, 500, 1000, 2000] #, 5000, 10000]     # 2000+ would make this crash

times_lin = []
times_qb = []

for size in sizes:
    target = 5
    numbers = [x for x in range(size)]
    elapsed_time_lin = []
    elapsed_time_qb = []
    for i in range(100):
        # alg 1
        elapsed_time_lin.append(timeit.timeit(lambda : linear_srch(numbers, target), number = 200))         # finds target 200x

        # alg 2
        current_time_qb = timeit.timeit(lambda : quicksort(numbers, 0, len(numbers)-1), number = 1)     # first sorts using quicksort
        current_time_qb += timeit.timeit(lambda : bsrch(numbers, 0, len(numbers)-1, target), number = 200)  # finds target 200x
        elapsed_time_qb.append(current_time_qb)

    print(f"The average time for linear search on an array of size {len(numbers)}: {sum(elapsed_time_lin)/100}")
    times_lin.append(sum(elapsed_time_lin)/100)
    print(f"The average time for quicksort + binary search on an array of size {len(numbers)}: {sum(elapsed_time_qb)/100}\n")
    times_qb.append(sum(elapsed_time_qb)/100)




# 6.5.4
    
xvals = np.array(sizes)
yvals_lin = np.array(times_lin)
yvals_qb = np.array(times_qb)

plt.plot(xvals, yvals_lin, label = 'Linear Search', color = 'red')
plt.plot(xvals, yvals_qb, label = 'Quicksort + Binary Search', color = 'blue')
plt.xlabel('Size')
plt.ylabel('Time')
plt.legend()
plt.show()

# Linear Search (algorithm 1) is faster than Quicksort + Binary Search (algorithm 2) in these tests. 
# (Arrays of size 2000+ were excluded because they would cause crashes even when setting the recursion limit to a high number.)
# The array is already sorted, which is the worst case for quicksort. 
# This makes it so that quicksort has much more recursive calls and takes much longer.
# Since the array is already sorted, the target (5) is close to the beginning of the array which makes
# linear search relatively fast.
