import random


#With the help of ChatGPT   
class Heap:
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

#Sorted Heap Test
sorted_array = [1, 3, 2, 5, 14, 4, 8, 6, 7, 18, 15, 17, 13, 16, 20, 11, 12, 10, 9, 19]
sorted_heap = Heap()
sorted_heap.heapify(sorted_array)
print(sorted_heap.heap) # Expected outcome: [1, 3, 2, 5, 14, 4, 8, 6, 7, 18, 15, 17, 13, 16, 20, 11, 12, 10, 9, 19]

#Empty Array Test
empty_array = []
empty_heap = Heap()
empty_heap.heapify(empty_array)
print(empty_heap.heap)  # Expected outcome: []

#Random Array Test
random_array = list(range(1, 30))
random.shuffle(random_array)
random_heap = Heap()
random_heap.heapify(random_array)
print(random_heap.heap)  