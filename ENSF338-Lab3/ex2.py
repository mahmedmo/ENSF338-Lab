import timeit
import random
def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr,low,high)
        quicksort(arr,low,pivot_index)
        quicksort(arr,pivot_index + 1, high)

def partition(arr, low, high):
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
size = 5;
arr = [[random.randint(1,100) for i in range(size + 10 * i)] for i in range(20)]

for x in range(20):
    timeit()