def merge_seperate(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]


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
 
        else:
            merged.append(right[right_index])
            right_index += 1

   
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

#Question 3
arr = [8, 42, 25, 3, 3, 1, 27, 3]
print(arr)
sorted_arr = merge_seperate(arr)
print(sorted_arr)


#Question 4
#Yes, the array splits in half in n steps to get each element alone.
#Then takes the elements and adds them up in a linear manner similar to the time complexity