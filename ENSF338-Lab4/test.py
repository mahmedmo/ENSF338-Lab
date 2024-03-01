def binary_search(array, target, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low <= high:
        mid = (low + high) // 2
        key = array[mid]

        if key == target:
            return mid
        elif key < target:
            return binary_search(array, target, mid + 1, high)  
        else:
            return binary_search(array, target, low, mid - 1)

    return -1 


sorted_array = [i for i in range(1, 1001)]
target_value = 789 

result = binary_search(sorted_array, target_value)

if result != -1:
    print(f"Target {target_value} found at index {result}.")
else:
    print(f"Target {target_value} not found in the array.")
 