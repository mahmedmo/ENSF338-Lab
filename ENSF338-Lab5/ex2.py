import random
import timeit
class PriorityQueue1:
    def __init__(self):
        self.queue = []
    def enqueue(self, val):
        self.queue.append(val)
        merge_sort(self.queue)
    def dequeue(self):
        if self.queue:
            self.queue.pop(0)
        else:
            return None

class PriorityQueue2:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        index = 0
        while index < len(self.queue) and self.queue[index] < element:
            index += 1
        self.queue.insert(index, element)

    def dequeue(self):
        if self.queue:
            self.queue.pop(0)
        else:
            return None

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    return merged


def generate_random_tasks():
    tasks = []
    for _ in range(1000):
        task = random.choices(["enqueue", "dequeue"], weights=[0.7, 0.3])[0]
        tasks.append(task)
    return tasks

pq1 = PriorityQueue1()
pq2 = PriorityQueue2()
taskList = []
for _ in range(100):
    taskList.append(generate_random_tasks())
print("Timing...")
def process_random_tasks(pq):
    for tasks in taskList:
        for task in tasks:
            if task == "enqueue":
                pq.enqueue(random.randint(1, 100))  
            elif task == "dequeue":
                pq.dequeue()

time_pq1 = timeit.timeit(lambda: process_random_tasks(pq1), number=1)
time_pq2 = timeit.timeit(lambda: process_random_tasks(pq2), number=1)

print(f"Time taken for PriorityQueue1: {time_pq1} seconds")
print(f"Time taken for PriorityQueue2: {time_pq2} seconds")

# Question 5
# PriorityQueue1 (implementation 1) takes a siginficant more amount of time compared to PriorityQueue2 (implementation 2).
# This is due to PriorityQueue1 calling the merge_sort function every time an element is appended, essentially sorting everytime. Additionally, 
# merge_sort is O(nlogn) and in comparison to PriorityQueue2 (implementation 2) sorts the queue as it gets appended so the worst
# case complexity is O(n) and O(n) is faster than O(nlogn) when compared at larger sizes of n which applies here.
