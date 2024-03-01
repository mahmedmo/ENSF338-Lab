import timeit
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# AI used to make Node and LinkedList classes
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_tail(self, new_data):
        new_node = Node(new_data)
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

    # Original reverse() implementation
    def reverse(self):
        newhead = None
        prevNode = None
        for i in range(self.get_size()-1, -1, -1):
            currNode = self.get_element_at_position(i)
            currNewNode = Node(currNode.data)
            if newhead is None:
                newhead = currNewNode
            else:
                prevNode.next = currNewNode
            prevNode = currNewNode
        self.head = newhead

    # ---ex7.2---
    # Optimized reverse() implementation
    def myreverse(self):
        currNode = self.head
        prevNode = None
        while currNode is not None:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
        self.head = prevNode


# ---ex7.3---
linked1000 = LinkedList()
for i in range(1000):
    linked1000.insert_tail(i)

linked2000 = LinkedList()
for i in range(2000):
    linked2000.insert_tail(i)

linked3000 = LinkedList()
for i in range(3000):
    linked3000.insert_tail(i)

linked4000 = LinkedList()
for i in range(4000):
    linked4000.insert_tail(i)

elapsed_time_reverse = []
elapsed_time_myreverse = []
# 1000
print("Running reverse() on linked list of size 1000...")
elapsed_time_reverse.append((timeit.timeit(lambda : linked1000.reverse(), number = 100))/100)
print("Running myreverse() on linked list of size 1000...")
elapsed_time_myreverse.append((timeit.timeit(lambda : linked1000.myreverse(), number = 100))/100)
# 2000
print("Running reverse() on linked list of size 2000...")
elapsed_time_reverse.append((timeit.timeit(lambda : linked2000.reverse(), number = 100))/100)       # THIS TAKES A BIT ~20s
print("Running myreverse() on linked list of size 2000...")
elapsed_time_myreverse.append((timeit.timeit(lambda : linked2000.myreverse(), number = 100))/100)
# 3000
print("Running reverse() on linked list of size 3000...")
elapsed_time_reverse.append((timeit.timeit(lambda : linked3000.reverse(), number = 100))/100)       # THIS TAKES A WHILE ~50s
print("Running myreverse() on linked list of size 3000...")
elapsed_time_myreverse.append((timeit.timeit(lambda : linked3000.myreverse(), number = 100))/100)
# 4000
print("Running reverse() on linked list of size 4000...")
elapsed_time_reverse.append((timeit.timeit(lambda : linked4000.reverse(), number = 100))/100)       # THIS TAKES A LONG WHILE ~100s
print("Running myreverse() on linked list of size 4000...")
elapsed_time_myreverse.append((timeit.timeit(lambda : linked4000.myreverse(), number = 100))/100)

print(elapsed_time_reverse, elapsed_time_myreverse)


# ---ex7.4---
sizes = [1000, 2000, 3000, 4000]

fig = plt.figure(figsize=(12, 10))

gs = gridspec.GridSpec(2, 2, height_ratios=[1, 1])
ax0 = plt.subplot(gs[0])
ax1 = plt.subplot(gs[1])
ax2 = plt.subplot(gs[2:])

# Plot for reverse()
ax0.plot(sizes, elapsed_time_reverse, label='reverse()', marker='o')
ax0.set_title('Sizes vs Times for reverse()')
ax0.set_xlabel('Sizes')
ax0.set_ylabel('Time for reverse()')

# Plot for myreverse()
ax1.plot(sizes, elapsed_time_myreverse, label='myreverse()', marker='o')
ax1.set_title('Sizes vs Times for myreverse()')
ax1.set_xlabel('Sizes')
ax1.set_ylabel('Time for myreverse()')

# Plot with both reverse() and myreverse()
ax2.plot(sizes, elapsed_time_myreverse, label='myreverse()', marker='o')
ax2.plot(sizes, elapsed_time_reverse, label='reverse()', marker='o')
ax2.set_title('Sizes vs Times')
ax2.set_xlabel('Sizes')
ax2.set_ylabel('Times')
ax2.legend()

plt.tight_layout()
plt.show()
