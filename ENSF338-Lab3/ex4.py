import timeit
import random
import sys 
import numpy as np
import matplotlib.pyplot as plt
def quicksort(arr, low, high):
    if low < high: 
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

#partition method aided via ChatGPT
def partition(arr, low, high):
    pivot = arr[high] 
    i = low - 1 
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  
    return i + 1
    
#ordered arrays with elements valued from 1- 100 with size 5 incremented by 10 in size each all in ascending order (sorted)
arr_sorted = [[i for i in range(i*10) ] for i in range(20)]
print(len(arr_sorted[19]))
quicksort_times = []
for x in range(20):
    #worse case quicksort: array is sorted (n^2)
    quicksort_times.append(timeit.timeit(lambda: quicksort(arr_sorted[x],0,len(arr_sorted[x]) -1),number=1))
    print("quicksort: pass",x+1)

sizes = [(i*10)for i in range(20)]  

#Insertion vs. Binary Insertion Plot
plt.plot(sizes, quicksort_times, label='Quicksort Sort (Worst Case)', marker='o')
plt.xlabel('Array Size')
plt.ylabel('Time (s)')
plt.legend()
plt.show()