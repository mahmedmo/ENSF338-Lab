import random
import matplotlib.pyplot as plt
import numpy as np

# ex3.2
def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                comparisons += 1
                swaps += 1
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
            else:
                comparisons += 1
    return arr, comparisons, swaps

# ex3.3

# makes an array of lists of increasing size from size 20 to 420, with jumps of 10. 
# each list has numbers from 1 to its size in random order.
arr = [random.sample(range(1,i+1), i) for i in range (20, 421, 10)]

size_list = [x for x in range (20, 421, 10)]
comps_list = []
swaps_list = []

print(f'{"size:":<10}{"comparisons:":<15}{"swaps:":<15}')
print('-'*40)
for i in range(0, 41):
    sorted_arr, comps, swps = bubble_sort(arr[i])
    comps_list.append(comps)
    swaps_list.append(swps)
    print(f'{len(arr[i]):<10}{comps:<15}{swps:<15}')

xvals = np.array(size_list)
yvals_comps = np.array(comps_list)
yvals_swaps = np.array(swaps_list)
# Fit polynomial functions to the data
comps_poly = np.polyfit(xvals, comps_list, 2)
swaps_poly = np.polyfit(xvals, swaps_list, 2)

# Generate interpolated values
comps_interp = np.polyval(comps_poly, xvals)
swaps_interp = np.polyval(swaps_poly, xvals)

# Create a figure with two subplots (2 rows, 1 column)
plt.figure(figsize=(10, 8))

# Plot the first subplot (comparisons)
plt.subplot(2, 1, 1)
plt.scatter(xvals, comps_list, label='Comparisons', color='red')
plt.plot(xvals, comps_interp, label='Interpolating Function', linestyle='--', color='orange')
plt.xlabel('# of Elements')
plt.ylabel('# of Comparisons')
plt.legend()

# Plot the second subplot (swaps)
plt.subplot(2, 1, 2)
plt.scatter(xvals, swaps_list, label='Swaps', color='blue')
plt.plot(xvals, swaps_interp, label='Interpolating Function', linestyle='--', color='cyan')
plt.xlabel('# of Elements')
plt.ylabel('# of Swaps')
plt.legend()

# Adjust layout for better spacing
plt.tight_layout()

# Show the plots
plt.show()