# Question 1
# The strategy to grow arrays when their size is full, is to resize the list.
# The resizing is done via the function "list_resize(list_resize(PyListObject *self, Py_ssize_t newsize)" on line 44.
# Essentially, what this function does is calculate a new size for the list when it needs to grow. It calculates this size
# to "new_allocated" which is greater than the required input to accomadate for future growth and it does this in multiples of 4.
# The formula used to achieve this (and is stored in new_allocated) is located on line 70 
# "new_allocated = ((size_t)newsize + (newsize >> 3) + 6) & ~(size_t)3;"
# This over allocates proprotional to the list size to the nearest multiple of 4. This results in a growth factor of (9/8) + 6. However, it approximately
# boils down to (9/8) as we get to larger sizes. Therefore, the growth factor is 1.125.

# Question 2
import sys
def list_growth(s):
    resize_arr = []
    prev_size = sys.getsizeof(resize_arr)
    for i in range(s):
        resize_arr.append(i)
        current_size = sys.getsizeof(resize_arr)
        print(f"Pass {i}: Size of list -{current_size/4} elements")
        if current_size != prev_size:
            print(f"Capacity changed at the {i} element: Previous size {prev_size/4} -> {current_size/4} elements")
            prev_size = current_size

list_growth(64)

# Question 3
import timeit
# Setup and statement code aided by ChatGPT
create_list ='''
S = 64
lst = [i for i in range(S)]
'''
grow_by_one = 'lst.append(S)'
growth_time = []
for x in range(1000):
    growth_time.append(timeit.timeit(setup=create_list, stmt=grow_by_one, number=1))
total_growth_time = sum(growth_time)
print(f"Growth time: {total_growth_time}")

# Question 4

shrink_by_one = 'lst.pop()'
shrink_time = []
for x in range(1000):
    shrink_time.append(timeit.timeit(setup=create_list, stmt=shrink_by_one, number=1))
total_shrink_time = sum(growth_time)
print(f"Shrink time: {total_shrink_time}")

#Question  5

import matplotlib.pyplot as plt
plt.figure(figsize=(12, 6))
plt.hist(growth_time, bins=30, alpha=0.5, label='Growth Time')
plt.hist(shrink_time, bins=30, alpha=0.5, color='r', label='Shrink Time')

plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.title('Distribution of Growth and Shrink Times')
plt.legend(loc='upper right')

plt.show()

# Why does Growth time frequently take longer than shrinking? This is because when Python needs to add 
# an element when the alloted space is full it must resize the array which can take complexity O(n) whereas
# when removing one element or popping space allocation isn't as much of an issue so it will consistently remain
# as complexity O(1)