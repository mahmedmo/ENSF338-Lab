import random
import timeit


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class ListPriorityQueue:
    def __init__(self):
        self.head = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None or data < self.head.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.data < data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def dequeue(self):
        if self.head is None:
            return None
        else:
            data = self.head.data
            self.head = self.head.next
            return data

    def peek(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

class HeapPriorityQueue:
    def __init__(self):
        self.heap = []

    def heapify(self, array):
        self.heap = array.copy()
        n = len(self.heap)

        for i in range(n // 2 - 1, -1, -1):
            self._heapify_down(i)

    def enqueue(self, element):
        self.heap.append(element)
        self._heapify_up(len(self.heap) - 1)

    def dequeue(self):
        if not self.heap:
            return None
        self._swap(0, len(self.heap) - 1)
        minimum = self.heap.pop()
        self._heapify_down(0)

        return minimum

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self._swap(index, parent_index)
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        n = len(self.heap)
        while index < n:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index

            if left_child_index < n and self.heap[left_child_index] < self.heap[smallest]:
                smallest = left_child_index
            if right_child_index < n and self.heap[right_child_index] < self.heap[smallest]:
                smallest = right_child_index

            if smallest != index:
                self._swap(index, smallest)
                index = smallest
            else:
                break

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


def generate_random_tasks():
    tasks = []
    for _ in range(1000):
        task = random.choices(["enqueue", "dequeue"], weights=[0.7, 0.3])[0]
        tasks.append(task)
    return tasks

def process_random_tasks(s):
    tasks = generate_random_tasks()
    for task in tasks:
        if task == "enqueue":
            s.enqueue(random.randint(1, 100))  
        elif task == "dequeue":
            s.dequeue()
q1 = ListPriorityQueue()
q2 = HeapPriorityQueue()
times_q1 = []
times_q2 = []
for _ in range(100):
    times_q1.append(timeit.timeit(lambda: process_random_tasks(q1), number=1))
    times_q2.append(timeit.timeit(lambda: process_random_tasks(q2), number=1))

print(f"Time taken for ListPriorityQueue: {sum(times_q1)} seconds")
print(f"Time taken for HeapPriorityQueue: {sum(times_q2)} seconds")

#Question 4
# HeapPriorityQueue is significally quicker than the ListPriorityQueue.
# This is becauses heaps structurally are already in a priority like order.
# Due to heaps' nature, you woulnd't need to search as much when dequeuing the smallest element unlike the linked-list.