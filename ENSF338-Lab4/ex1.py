import random
import sys
import timeit

import matplotlib.pyplot as plt

sys.setrecursionlimit(30000)

#Question 1
class ListNode:
    def __init__(self, value):
        self.data = value
        self.next = None

    def getData(self):
        return self._value

    def setData(self, value):
        self._value = value

    def getNext(self):
        return self._next

    def setNext(self, next):
        self._next = next

    def toString(self):
        return str(self._value)
    
  
#Question 2
def newNode(x):

    temp = ListNode(0)
    temp.data = x
    temp.next = None
    return temp

def binary_search(head, value):
    start = head
    last = None
    while True:
        mid = middle(start, last)
        if (mid == None):
            return None
        if (mid.data == value):
            return mid
        elif (mid.data < value):
            start = mid.next
        else:
            last = mid
        if not (last == None or last != start):
            break
    return None

def middle(start, last):
    if not start:
        return None
    slow = start
    fast = start.next

    while fast != last:
        fast = fast.next
        if fast != last:
            slow = slow.next
            fast = fast.next

    return slow


#With the help of ChatGPT
def create_linked_list(size):
    head = newNode(0)
    current = head
    for i in range(1, size):
        current.next = newNode(i)
        current = current.next
    return head

def measure_average_case(size):
    linked_list_head = create_linked_list(size)
    target_value = random.randint(0, size - 1)
    time_taken = timeit.timeit(lambda: binary_search(linked_list_head, target_value), number=1000)
    return time_taken

# List of input sizes
input_sizes = [1000, 2000, 4000, 8000]

# Measure average-case performance for each input size
average_times = [measure_average_case(size) for size in input_sizes]

# Plotting the results
plt.plot(input_sizes, average_times, marker='o')
plt.title('Average-case Performance of Binary Search on Linked List')
plt.xlabel('Linked List Size')
plt.ylabel('Average Time (seconds)')
plt.show()