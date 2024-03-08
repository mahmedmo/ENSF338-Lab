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

def time_vector_bst(vector, root):
    total_time = 0
    average_time = 0
    for lookup in vector:
            time_taken = timeit.timeit(lambda: search(lookup, root), number=10)
            total_time += time_taken
    average_time = total_time / len(vector)
    return average_time, total_time

vector = list(range(10000))
root = initialize_tree(vector) 
random.shuffle(vector)
root = initialize_tree(vector) 
average_time, total_time = time_vector_bst(vector, root)
print(f"SHUFFLED VECTOR (BST): Average to insert a single element {average_time}")
print(f"SHUFFLED VECTOR (BST): Total time across inserting each element 10 times {total_time}")

# QUESTION 3
def time_vector_bs(vector):
    total_time = 0
    average_time = 0
    for lookup in vector:
            time_taken = timeit.timeit(lambda: binary_search(vector, lookup), number=10)
            total_time += time_taken
    average_time = total_time / len(vector)
    return average_time, total_time

def binary_search(array, target):
    low = 0
    high = len(array) - 1
    
    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]
        
        if guess == target:
            return mid  
        if guess < target:
            low = mid + 1  
        else:
            high = mid - 1
    return None
  
vector.sort()
average_time, total_time = time_vector_bs(vector)
print(f"SORTED VECTOR (ARRAY with Binary Search): Average to insert a single element {average_time}")
print(f"SORTED VECTOR (ARRAY with Binary Search): Total time across inserting each element 10 times {total_time}")

#QUESTION 4
# The times for both came very close. The results showed that the binary search tree won by a slight margin. This is a bit tougher to really
# decide which implementation is faster, considering both use a form of binary search. However, I believe that the binary search tree was
# faster due to the nature of the data structure used itself. It uses nodes and is able to traverse through the data very fast and with a balanced enough
# tree, it yields faster than the array implementation, this occurs due to a lesser depth within the strucutre. 
# Overall, both implementations yielded O(log n) in this test.