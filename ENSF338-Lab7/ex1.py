import timeit
import random
# Question 1
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

def initialize_tree(vector):
    root = None
    for item in vector:
        root = insert(item, root)
    return root

# Question 2
def get_balance(node):
    if node is None:
        return 0  
    return height(node.right) - height(node.left)

def height(node):
    if node is None:
        return 0 
    return 1 + max(height(node.left), height(node.right))


def print_balances(node):
    if node is None:
        return

    print("Balance factor of node with data", node.data, ":", get_balance(node))
    print_balances(node.left)
    print_balances(node.right)

# Question 3
roots = []
vector = list(range(1000))
for x in range(1000):
    random.shuffle(vector)
    root = initialize_tree(vector) 
    roots.append(root)

# Question 4
abs_balances = []
avg_balances = []
balance_test_times = []

def balance_test(root):
    balance_factors = []
    for x in range(len(vector)):
        node = search(vector[x],root)
        balance_factors.append(get_balance(node))
    avg_balances.append(sum(balance_factors)/len(balance_factors))
    abs_balances.append(max(max(balance_factors),-1*min(balance_factors)))

for root in roots:
    balance_test_times.append(timeit.timeit(lambda:balance_test(root),number=1))
# Question 5
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
plt.scatter(abs_balances, balance_test_times, color='blue', alpha=0.7)
plt.xlabel('Absolute Balances')
plt.ylabel('Search Time (Balance Test Times)')
plt.title('Scatterplot of Absolute Balances vs Search Time')
plt.grid(True)
plt.show()


