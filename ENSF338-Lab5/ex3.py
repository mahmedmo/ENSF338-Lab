import random
import timeit
import matplotlib.pyplot as plt
class Stack1:
    def __init__(self):
        self.stack = []
    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.stack:
            self.stack.pop()
class Node:
    def __init__(self,val):
        self.value = val
        self.next = None
class Stack2:
    def __init__(self):
        self.head = None
    
    def push(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node  
        return
    
    def pop(self):
        if self.head:
            self.head = self.head.next
        return


def generate_random_tasks():
    tasks = []
    for _ in range(10000):
        task = random.choices(["push", "pop"], weights=[0.7, 0.3])[0]
        tasks.append(task)
    return tasks

s1 = Stack1()
s2 = Stack2()

def process_random_tasks(s):
    tasks = generate_random_tasks()
    for task in tasks:
        if task == "push":
            s.push(random.randint(1, 100))  
        elif task == "pop":
            s.pop()
times_s1 = []
times_s2 = []
for _ in range(100):
    times_s1.append(timeit.timeit(lambda: process_random_tasks(s1), number=1))
    times_s2.append(timeit.timeit(lambda: process_random_tasks(s2), number=1))

print(f"Time taken for Stack1: {sum(times_s1)} seconds")
print(f"Time taken for Stack2: {sum(times_s2)} seconds")
# Plotting 
    
plt.figure(figsize=(10, 6))
plt.hist(times_s1, bins=20, alpha=0.5, label='Stack1 (List)')
plt.hist(times_s2, bins=20, alpha=0.5, label='Stack2 (Linked List)')
plt.xlabel('Execution Time (seconds)')
plt.ylabel('Frequency')
plt.legend(loc='upper right')
plt.title('Distribution of Execution Times for Stack Implementations')
plt.show()

# Question 5
# The built in python lists performed faster than the LinkedList by a small margin.
# This can be due to the added stress with the LinkedList with how it manages pointer references.
# Additonally, Python has very fast built in functions as they are considerably optimized and refined.