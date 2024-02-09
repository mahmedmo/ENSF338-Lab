import timeit
import random
import sys 
import numpy as np
import matplotlib.pyplot as plt
sys.setrecursionlimit(20000)

def quicksort(arr, low, high):
    if low < high:
        pivot = partition(arr,low,high)
        quicksort(arr,low,pivot)
        quicksort(arr,pivot+1,high)

def partition(arr,low,high):
    pivot = arr[low]
    left = low + 1
    right = high
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while arr[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right
    

def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if(arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr
size = 1
#randomized arrays with elements valued from 1- 100 with size 5 incremented by each subsequent array
arr_random = [[random.randint(1,100) for i in range(size + i)] for i in range(20)]
print(len(arr_random[19]))
size = 1
#ordered arrays with elements valued from 1- 100 with size 5 incremented by each subsequent array all in ascending order (sorted)
arr_sorted = [[i for i in range(size + i) ] for i in range(20)]
print(len(arr_sorted[19]))
size = 1
#ordered arrays with elements valued from 1- 100 with size 5 incremented by each subsequent array all in descending order (reverse_sorted)
arr_reverse_sorted = [[i for i in range(size + i -1,-1,-1)] for i in range(20)]
print(len(arr_reverse_sorted[19]))
worse_quicksort = []
average_quicksort = []
best_quicksort = []
worse_bubblesort = []
average_bubblesort = []
best_bubblesort = []
for x in range(20):
    #worse case quicksort: array is sorted (n^2)
    worse_quicksort.append(timeit.timeit(lambda: quicksort(arr_sorted[x],0,len(arr_sorted[x]) -1)))
    print("worse_quicksort: pass",x)
    #average case quicksort random array (nlog(n))
    average_quicksort.append(timeit.timeit(lambda: quicksort(arr_random[x],0,len(arr_random[x]) -1)))
    print("pass",x)
    #best case quicksort random array (nlog(n))
    best_quicksort.append(timeit.timeit(lambda: quicksort(arr_random[x],0,len(arr_random[x]) -1))) 
    print("pass",x)
    #worse case quicksort: array is sorted O(n^2)
    worse_bubblesort.append(timeit.timeit(lambda: bubblesort(arr_reverse_sorted[x])))
    #average case bubblesort random array O(n^2)
    average_bubblesort.append(timeit.timeit(lambda: bubblesort(arr_random[x])))
    #best case bubblesort random array O(n)
    best_bubblesort.append(timeit.timeit(lambda: bubblesort(arr_sorted[x])))
    print("pass",x)
print(worse_quicksort)
print(average_quicksort)
print(best_quicksort)
print(worse_bubblesort)
print(average_bubblesort)
print(best_bubblesort)

sizes = [1 + i for i in range(20)]  


fig, axs = plt.subplots(3, 1, figsize=(10, 15))


axs[0].plot(sizes, worse_quicksort, label='Quicksort (Worst Case)', marker='o')
axs[0].plot(sizes, worse_bubblesort, label='Bubblesort (Worst Case)', marker='x')
axs[0].set_title('Worst Case Performance')
axs[0].set_xlabel('Array Size')
axs[0].set_ylabel('Time (s)')
axs[0].legend()


axs[1].plot(sizes, average_quicksort, label='Quicksort (Average Case)', marker='o')
axs[1].plot(sizes, average_bubblesort, label='Bubblesort (Average Case)', marker='x')
axs[1].set_title('Average Case Performance')
axs[1].set_xlabel('Array Size')
axs[1].set_ylabel('Time (s)')
axs[1].legend()


axs[2].plot(sizes, best_quicksort, label='Quicksort (Best Case)', marker='o')
axs[2].plot(sizes, best_bubblesort, label='Bubblesort (Best Case)', marker='x')
axs[2].set_title('Best Case Performance')
axs[2].set_xlabel('Array Size')
axs[2].set_ylabel('Time (s)')
axs[2].legend()

plt.tight_layout()
plt.show()
