def merge_seperate(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    print("Split: ", (left))
    right = arr[mid:]
    print("Split: ", (right))

    left = merge_seperate(left)
    right = merge_seperate(right)
    
    return merge(left, right)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
            print("Merge: ", (merged))  #Question 3
        else:
            merged.append(right[right_index])
            right_index += 1
            print("Merge: ", (merged)) #Question 3
   
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

#Question 2
#The code written does have a time complexity of O(n log(n)) 
#Firstly the function 'merge_seperate' will go on to divide in half n times for all the elements seperated.
#Then 'merge' compares the left and right elements together and merges them into one subarray.
#Next step the subarrays will be compared and swap around until sorted and create a bigger subarray and will keep going until the full array is sorted.

#Question 3
arr = [8, 42, 25, 3, 3, 1, 27, 3]
print(arr)
sorted_arr = merge_seperate(arr)
print(sorted_arr)

#Question 4
#Yes, the array splits in half in n steps to get each element alone.
#Then takes the elements and adds them up in a linear manner similar to the time complexity