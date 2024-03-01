import random
import sys
import timeit

import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt

sys.setrecursionlimit(30000)

# Question 1
class ListNode:
    def __init__(self, value):
        self.data = value
        self.next = None

    def getData(self):
        return self.data

    def setData(self, value):
        self.data = value

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next

    def toString(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_tail(self, new_data):
        new_node = ListNode(new_data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    def get_size(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count

    def get_element_at_position(self, pos):
        curr = self.head
        count = 0
        while curr:
            if count == pos:
                return curr
            count += 1
            curr = curr.next
        return None

    def display(self):
        elements = []
        currNode = self.head
        while currNode:
            elements.append(currNode.data)
            currNode = currNode.next
        return elements

# Question 2
def binary_search_linked_list(head, value):
    start = head
    last = None
    while True:
        mid = middle(start, last)
        if mid is None:
            return None
        if mid.data == value:
            return mid
        elif mid.data < value:
            start = mid.next
        else:
            last = mid
        if not (last is None or last != start):
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

# Question 3
class Array:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def __getitem__(self, index):
        if 0 <= index < self.size:
            return self.data[index]
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, index, value):
        if 0 <= index < self.size:
            self.data[index] = value
        else:
            raise IndexError("Index out of range")

    def __len__(self):
        return self.size

    def __repr__(self):
        return repr(self.data)

def binary_search_array(arr, value):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == value:
            return mid
        elif mid_value < value:
            low = mid + 1
        else:
            high = mid - 1

    return None

# Question 4
# The time complexity when performing a binary search on a linked list should be O(n) where n represents the number of nodes.

# Question 5
# With the help of ChatGPT
# Function to measure the average-case performance

sizes = [1000, 2000, 4000, 8000]
linked1000 = LinkedList()
for i in range(1000):
    linked1000.insert_tail(i)

linked2000 = LinkedList()
for i in range(2000):
    linked2000.insert_tail(i)

linked4000 = LinkedList()
for i in range(4000):
    linked4000.insert_tail(i)

linked8000 = LinkedList()
for i in range(8000):
    linked8000.insert_tail(i)

array1000 = Array(1000)
for i in range(1000):
    array1000[i] = i

array2000 = Array(2000)
for i in range(2000):
    array2000[i] = i

array4000 = Array(4000)
for i in range(4000):
    array4000[i] = i

array8000 = Array(8000)
for i in range(8000):
    array8000[i] = i

value_1000 = random.randint(0,1000)
value_2000 = random.randint(0,2000)
value_4000 = random.randint(0,4000)
value_8000 = random.randint(0,8000)

elapsed_time_list = []
elapsed_time_array = []

# 1000
elapsed_time_list.append((timeit.timeit(lambda: binary_search_linked_list(linked1000.head, value_1000), number=1000))/1000)
elapsed_time_array.append((timeit.timeit(lambda: binary_search_array(array1000.data, value_1000), number=1000))/1000)

# 2000
elapsed_time_list.append((timeit.timeit(lambda: binary_search_linked_list(linked2000.head, value_2000), number=1000))/1000)
elapsed_time_array.append((timeit.timeit(lambda: binary_search_array(array2000.data, value_2000), number=1000))/1000)

# 4000
elapsed_time_list.append((timeit.timeit(lambda: binary_search_linked_list(linked4000.head, value_4000), number=1000))/1000)
elapsed_time_array.append((timeit.timeit(lambda: binary_search_array(array4000.data, value_4000), number=1000))/1000)

# 8000
elapsed_time_list.append((timeit.timeit(lambda: binary_search_linked_list(linked8000.head, value_8000), number=1000))/1000)
elapsed_time_array.append((timeit.timeit(lambda: binary_search_array(array8000.data, value_8000), number=1000))/1000)

print("List Times", elapsed_time_list)
print("Array Times", elapsed_time_array)


#Question 6
# Array times looks flat but this may be due to Linked List times being that much slower than Array times.

plt.figure(figsize=(10, 6))
plt.plot(sizes, elapsed_time_list, label='linkedlist()', marker='o')
plt.plot(sizes, elapsed_time_array, label='array()', marker='o')
plt.xlabel('Size')
plt.ylabel('Times')
plt.legend()
plt.title('Performance of Binary Search')
plt.show()
