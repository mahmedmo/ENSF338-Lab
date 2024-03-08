#Question 1
class CircularQueueArray:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, element):
        if self.is_full():
            print("enqueue None")
            return

        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity

        self.queue[self.rear] = element
        print(f"enqueue {element}")

    def dequeue(self):
        if self.is_empty():
            print("dequeue None")
            return None

        element = self.queue[self.front]

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity

        print(f"dequeue {element}")
        return element

    def peek(self):
        if self.is_empty():
            print("peek None")
            return None

        element = self.queue[self.front]
        print(f"peek {element}")
        return element

#Question 2
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class CircularLinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, element):
        new_node = Node(element)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
            print("enqueue None")
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
            print(f"enqueue {element}")

    def dequeue(self):
        if not self.is_empty():
            if self.head == self.tail:
                data = self.head.data
                self.head = None
                self.tail = None
                print(f"dequeue None")
            else:
                data = self.head.data
                self.head = self.head.next
                self.tail.next = self.head
                print(f"dequeue {data}")
            return data
        else:
            print(f"dequeue None")

    def is_empty(self):
        return self.head is None

    def size(self):
        if self.is_empty():
            return 
        count = 1
        current = self.head.next
        while current != self.head:
            count += 1
            current = current.next
        return count
    
    def peek(self):
        if not self.is_empty():
            data = self.head.data
            print(f"peek {data}")
            return self.head.data
        else:
            print(f"peek None")
            
#Question 3
myarray = CircularQueueArray(12)
print('Operations for Array Queue')
myarray.enqueue(1)  # enqueue 1
myarray.enqueue(2)  # enqueue 2
myarray.enqueue(3)  # enqueue 3
myarray.enqueue(4)  # enqueue 4
myarray.enqueue(5)  # enqueue 5

# Peek operation
myarray.peek()      # peek 1

# Dequeue operationn
myarray.dequeue()   # dequeue 1
myarray.dequeue()   # dequeue 2

#Enqueue more elements
myarray.enqueue(6)  # enqueue 6
myarray.enqueue(7)  # enqueue 7
myarray.enqueue(8)  # enqueue 8

# Peek operation
myarray.peek()      # peek 3

# Dequeue operations
myarray.dequeue()   # dequeue 3
myarray.dequeue()   # dequeue 4

# Enqueue more elements
myarray.enqueue(9)  # enqueue 9
myarray.enqueue(10) # enqueue 10
myarray.enqueue(11) # enqueue 11

# Peek operation
myarray.peek()      # peek 5

# Enqueue more elements
myarray.enqueue(12) # enqueue 12
myarray.enqueue(13) # enqueue 13
myarray.enqueue(14) # enqueue 14
myarray.enqueue(15) # enqueue 15
myarray.enqueue(16) # enqueue 16

# Attempting to enqueue a full Array
myarray.enqueue(17) # enqueue None

#Dequeue operations
myarray.dequeue()   # dequeue 5
myarray.dequeue()   # dequeue 6
myarray.dequeue()   # dequeue 7
myarray.dequeue()   # dequeue 8
myarray.dequeue()   # dequeue 9
myarray.dequeue()   # dequeue 10
myarray.dequeue()   # dequeue 11
myarray.dequeue()   # dequeue 12
myarray.dequeue()   # dequeue 13
myarray.dequeue()   # dequeue 14
myarray.dequeue()   # dequeue 15
myarray.dequeue()   # dequeue 16

# Attempting to dequeue an empty Array
myarray.dequeue()   # Queue is empty. Cannot dequeue.

# Attempting to peek an empty Array
myarray.peek()      # Queue is empty. Cannot peek.

mylist = CircularLinkedListQueue()
print('Operations for Circular List Queue')
# Enqueue operations
mylist.enqueue(1)  # enqueue 1
mylist.enqueue(2)  # enqueue 2
mylist.enqueue(3)  # enqueue 3
mylist.enqueue(4)  # enqueue 4
mylist.enqueue(5)  # enqueue 5

# Peek operation
mylist.peek()      # peek 1

# Dequeue operationn
mylist.dequeue()   # dequeue 1
mylist.dequeue()   # dequeue 2

#Enqueue more elements
mylist.enqueue(6)  # enqueue 6
mylist.enqueue(7)  # enqueue 7
mylist.enqueue(8)  # enqueue 8

# Peek operation
mylist.peek()      # peek 3

# Dequeue operations
mylist.dequeue()   # dequeue 3
mylist.dequeue()   # dequeue 4

# Enqueue more elements
mylist.enqueue(9)  # enqueue 9
mylist.enqueue(10) # enqueue 10
mylist.enqueue(11) # enqueue 11

# Peek operation
mylist.peek()      # peek 5


mylist.enqueue(12) # enqueue 12
mylist.enqueue(13) # enqueue 13
mylist.enqueue(14) # enqueue 14
mylist.enqueue(15) # enqueue 15

# Peek operation
mylist.peek()      # peek 5

# Dequeue operations
mylist.dequeue()   # dequeue 5

# Enqueue more elements
mylist.enqueue(16) # enqueue 16
mylist.enqueue(17) # enqueue 17
mylist.enqueue(18) # enqueue 18

# Peek operation
mylist.peek()      # peek 6

# Dequeue operation
mylist.dequeue()   # dequeue 6

# Peek operation
mylist.peek()      # peek 7

#Dequeue operations
mylist.dequeue()   # dequeue 7
mylist.dequeue()   # dequeue 8
mylist.dequeue()   # dequeue 9
mylist.dequeue()   # dequeue 10
mylist.dequeue()   # dequeue 11
mylist.dequeue()   # dequeue 12
mylist.dequeue()   # dequeue 13
mylist.dequeue()   # dequeue 14
mylist.dequeue()   # dequeue 15
mylist.dequeue()   # dequeue 16
mylist.dequeue()   # dequeue 17

# Attempting to dequeue from an empty queue
mylist.dequeue()   # Queue is empty. Cannot dequeue.

# Attempting to peek an empty queue
mylist.peek()      # Queue is empty. Cannot peek.




