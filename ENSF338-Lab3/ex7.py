import sys 
sys.setrecursionlimit(30000)

def binary_search(arr, target, start):
    low, high = start, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1 
        else:
            high = mid - 1  

    return -1

sorted_arr = 
target = 
start_midpoint =

result = binary_search(sorted_arr, target, start_midpoint)

if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found in the array.")