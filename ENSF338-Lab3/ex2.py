import timeit
import random
import sys 
import numpy as np
import matplotlib.pyplot as plt
sys.setrecursionlimit(20000)

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
    

def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if(arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr
#randomized arrays with elements valued from 1- 100 incremented by 10 in size each
arr_random = [[random.randint(1,100) for i in range(i*10)] for i in range(20)]
print(len(arr_random[19]))
#ordered arrays with elements valued from 1- 100 with size 5 incremented by 10 in size each all in ascending order (sorted)
arr_sorted = [[i for i in range(i*10) ] for i in range(20)]
print(len(arr_sorted[19]))
#ordered arrays with elements valued from 1- 100 with size 5 incremented by 10 in size each all in descending order (reverse_sorted)
arr_reverse_sorted = [[i for i in range((i*10)-1,-1,-1)] for i in range(20)]
print(len(arr_reverse_sorted[19]))
worse_quicksort = []
average_best_quicksort = []
worse_bubblesort = []
average_bubblesort = []
best_bubblesort = []
for x in range(20):
    #worse case quicksort: array is sorted (n^2)
    worse_quicksort.append(timeit.timeit(lambda: quicksort(arr_sorted[x],0,len(arr_sorted[x]) -1),number=1))
    print("worse_quicksort: pass",x+1)
    #average/best case quicksort random array (nlog(n))
    average_best_quicksort.append(timeit.timeit(lambda: quicksort(arr_random[x],0,len(arr_random[x]) -1),number=1))
    print("average_best_quicksort: pass",x+1)
    #worse case quicksort: array is sorted O(n^2)
    worse_bubblesort.append(timeit.timeit(lambda: bubblesort(arr_reverse_sorted[x]),number=1))
    print("worse_bubblesort: pass",x+1)
    #average case bubblesort random array O(n^2)
    average_bubblesort.append(timeit.timeit(lambda: bubblesort(arr_random[x]),number=1))
    print("average_bubblesort: pass",x+1)
    #best case bubblesort random array O(n)
    best_bubblesort.append(timeit.timeit(lambda: bubblesort(arr_sorted[x]),number=1))
    print("best_bubblesort: pass",x+1)


sizes = [(i*10) for i in range(20)]  


#Worst Case Performance
plt.figure(figsize=(10, 5))
plt.plot(sizes, worse_quicksort, label='Quicksort (Worst Case)', marker='o')
plt.plot(sizes, worse_bubblesort, label='Bubblesort (Worst Case)', marker='x')
plt.title('Worst Case Performance')
plt.xlabel('Array Size')
plt.ylabel('Time (s)')
plt.legend()
plt.show()

#Average Case Performance
plt.figure(figsize=(10, 5))
plt.plot(sizes, average_best_quicksort, label='Quicksort (Average Case)', marker='o')
plt.plot(sizes, average_bubblesort, label='Bubblesort (Average Case)', marker='x')
plt.title('Average Case Performance')
plt.xlabel('Array Size')
plt.ylabel('Time (s)')
plt.legend()
plt.show()

#Best Case Performance
plt.figure(figsize=(10, 5))
plt.plot(sizes, average_best_quicksort, label='Quicksort (Best Case)', marker='o')
plt.plot(sizes, best_bubblesort, label='Bubblesort (Best Case)', marker='x')
plt.title('Best Case Performance')
plt.xlabel('Array Size')
plt.ylabel('Time (s)')
plt.legend()
plt.show()