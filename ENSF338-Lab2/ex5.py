import random
import timeit
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
array1 = [4,6,10,44,76,12,90,3,1,223]
vector8 = [x for x in range(0,8000)]
vector16 = [x for x in range(0,16000)]
vector32 = [x for x in range(0,32000)]
def linear(arr,value):
    for x in range(len(arr)):
        if arr[x] == value:
            return x

def binary_search(arr,value):
    left = 0
    right = len(arr) -1
    while left <= right:
        mid = (left+right)//2
        if(arr[mid] == value):
            return mid
        elif(value > arr[mid]):
            left = mid + 1
        elif(value < arr[mid]):
            right = mid -1
    return -1

print(linear(array1,12))
print(binary_search(array1,44))

print("Linear Search: 8000 Elements... ")
elapsed_time = timeit.timeit(lambda: linear(vector8,random.randint(0, 7999)), number=100)
print("Average time:", elapsed_time/100)

print("Linear Search: 16000 Elements... ")
elapsed_time = timeit.timeit(lambda: linear(vector16,random.randint(0, 15999)), number=100)
print("Average time:", elapsed_time/100)

print("Linear Search: 32000 Elements... ")
elapsed_time = timeit.timeit(lambda: linear(vector32,random.randint(0, 31999)), number=100)
print("Average time:", elapsed_time/100)

print("Binary Search: 8000 Elements... ")
elapsed_time = timeit.timeit(lambda: binary_search(vector8,random.randint(0, 7999)), number=100)
print("Average time:", elapsed_time/100)

print("Binary Search: 16000 Elements... ")
elapsed_time = timeit.timeit(lambda: binary_search(vector16,random.randint(0, 15999)), number=100)
print("Average time:", elapsed_time/100)

print("Binary Search: 32000 Elements... ")
elapsed_time = timeit.timeit(lambda: binary_search(vector32,random.randint(0, 31999)), number=100)
print("Average time:", elapsed_time/100)

#Plotting 
sizes = np.array([8000, 16000, 32000])
linear_avg_times = np.array([
    timeit.timeit(lambda: linear(vector8, random.randint(0, 7999)), number=100) / 100,
    timeit.timeit(lambda: linear(vector16, random.randint(0, 15999)), number=100) / 100,
    timeit.timeit(lambda: linear(vector32, random.randint(0, 31999)), number=100) / 100
])
binary_avg_times = np.array([
    timeit.timeit(lambda: binary_search(vector8, random.randint(0, 7999)), number=100) / 100,
    timeit.timeit(lambda: binary_search(vector16, random.randint(0, 15999)), number=100) / 100,
    timeit.timeit(lambda: binary_search(vector32, random.randint(0, 31999)), number=100) / 100
])

def linear_fit(x, a, b):
    return a * x + b

def logarithmic_fit(x, a, b):
    return a * np.log(x) + b

linear_params, _ = curve_fit(linear_fit, sizes, linear_avg_times)
binary_params, _ = curve_fit(logarithmic_fit, sizes, binary_avg_times)

x_values = np.linspace(8000, 32000, 400)
linear_curve = linear_fit(x_values, *linear_params)
binary_curve = logarithmic_fit(x_values, *binary_params)

# Code to plot aided by ChatGPT
plt.figure(figsize=(14, 7))

plt.subplot(1, 2, 1)
plt.scatter(sizes, linear_avg_times, color='blue', label='Linear Search Times')
plt.plot(x_values, linear_curve, 'r--', label=f'Linear Fit: y = {linear_params[0]:.5f}x + {linear_params[1]:.5f}')
plt.title('Linear Search Time Complexity')
plt.xlabel('Array Size')
plt.ylabel('Average Time (seconds)')
plt.legend()

plt.subplot(1, 2, 2)
plt.scatter(sizes, binary_avg_times, color='green', label='Binary Search Times')
plt.plot(x_values, binary_curve, 'r--', label=f'Log Fit: y = {binary_params[0]:.5f}log(x) + {binary_params[1]:.5f}')
plt.title('Binary Search Time Complexity')
plt.xlabel('Array Size')
plt.ylabel('Average Time (seconds)')
plt.legend()

plt.tight_layout()
plt.show()

# Question 4 Answer

# The results are expected, since with binary search, every sequential search done using 
# this algorithm halves the number of elements it has to search through, resulting in 
# logarithmic function and shorter times. For linear search, it scans starting from the first 
# index up until the end, taking a much longer time and therefore resulting in a linear 
# function. This leaves the logarithmic function: y = alog(x) + b, with a being the rate at 
# which the search time increases with the logarithm of the array size and b is the search 
# time when the size of the array is at the base of the logarithm used. This leaves this 
# function with a big O complexity of O(log(n)). As for the linear function y = ax+b, where
# a represents the rate at which the search time increases with the array size and b is the 
# base search time for an array of size zero. This leaves the linear search algorithm with a 
# big O complexity of O(n)