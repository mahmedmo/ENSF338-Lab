import random
import timeit

import matplotlib.pyplot as plt


#Question 1
class Queue1:
    def __init__(self):
        self.queue = []
 
    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop()
    

#Question 2
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Queue2:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.tail is not None:
            self.tail.next = new_node
        self.tail = new_node
        if self.head is None:
            self.head = self.tail

    def dequeue(self):
        if self.is_empty():
            return None
        
        if not self.is_empty():
            current = self.head
            prev = None

            while current.next:
                prev = current
                current = current.next

            if prev:
                prev.next = None
                self.tail = prev

            else:
                self.head = None
                self.tail = None

            return current.data

    def is_empty(self):
        return self.head is None

q1 = Queue1()
q2 = Queue2()
#Question 3
def generate_random_tasks():
    tasks = []
    for _ in range(10):
        task = random.choices(["enqueue", "dequeue"], weights=[0.7, 0.3])[0]
        print(task)
        tasks.append(task)
    return tasks

def process_random_tasks(s):
    tasks = generate_random_tasks()
    for task in tasks:
        if task == "enqueue":
            s.enqueue(random.randint(1, 100))  
        elif task == "dequeue":
            s.dequeue()
#Question 4
times_q1 = []
times_q2 = []
for _ in range(100):
    times_q1.append(timeit.timeit(lambda: process_random_tasks(q1), number=1))
    times_q2.append(timeit.timeit(lambda: process_random_tasks(q2), number=1))

print(f"Time taken for Queue1: {sum(times_q1)} seconds")
print(f"Time taken for Queue2: {sum(times_q2)} seconds")

#Question 5
plt.figure(figsize=(10, 6))
plt.hist(times_q1, bins=20, alpha=0.5, label='Queue1 (Array)')
plt.hist(times_q2, bins=20, alpha=0.5, label='Queue2 (Singly-Linked List)')
plt.xlabel('Execution Time (seconds)')
plt.ylabel('Frequency')
plt.legend(loc='upper right')
plt.title('Distribution of Execution Times for Queue Implementations')
plt.show()
