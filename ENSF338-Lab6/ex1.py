import timeit
import random

# QUESTION 1
class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right

def insert(data, root=None):
    if root is None:
        return Node(data)  

    current = root
    parent = None

    while current is not None:
        parent = current
        if data <= current.data:
            current = current.left
        else:
            current = current.right

    newnode = Node(data, parent)
    if data <= parent.data:
        parent.left = newnode
    else:
        parent.right = newnode

    return root  

def search(data, root):
    current = root
    while current is not None:
        if data == current.data:
            return current
        elif data < current.data:
            current = current.left
        else:
            current = current.right
    return None

# QUESTION 2 

def initialize_tree(vector):
    root = None
    for item in vector:
        root = insert(item, root)
    return root

def time_vector(vector, root):
    total_time = 0
    average_time = 0
    for lookup in vector:
            time_taken = timeit.timeit(lambda: search(lookup, root), number=10)
            total_time += time_taken
    average_time = total_time / len(vector)
    return average_time, total_time

vector = list(range(10000))
root = initialize_tree(vector) 
average_time, total_time = time_vector(vector, root)
print(f"SORTED VECTOR: Average time to insert a single element  {average_time}")
print(f"SORTED VECTOR: Total time across inserting each element 10 times {total_time}")

# QUESTION 3 
random.shuffle(vector)
root = initialize_tree(vector) 
average_time, total_time = time_vector(vector, root)
print(f"SHUFFLED VECTOR: Average to insert a single element {average_time}")
print(f"SHUFFLED VECTOR: Total time across inserting each element 10 times {total_time}")

# # QUESTION 4
# The results show that the time it takes to searh a binary tree created from a shuffled list 
# to be much faster than that of a sorted list. This occurs because when adding elements that are sorted
# due to the way the comparisions work in insertion. The tree degenerates to an extent to a linked list causing 
# a great imbalance in the tree. Therefore when searching through the list the complexity is closer to O(n) instead
# of O(log n) (the complexity that occurs with a balanced tree).