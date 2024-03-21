import timeit
import random
# Question 1
class Node:
    def __init__(self, data, left=None, right=None, height=1):
        self.data = data
        self.left = left
        self.right = right
        self.height = height

class BSTTree(object):
    def insert(self, root, data):
        if not root:
            return Node(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))  
        return root
    
    def search(self, data, root):
        current = root
        while current is not None:
            if data == current.data:
                return current
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return None
    
    def get_height(self, root):
        if not root:
            return 0

        return root.height

    def get_balance(self, root):
        if not root:
            return 0

        return self.get_height(root.left) - self.get_height(root.right)
    
    # For self testing
    def pre_order(self, root):
        if not root:
            return
        print("{0} ".format(root.data), end="")
        self.pre_order(root.left)
        self.pre_order(root.right)

BSTTree = BSTTree()

def initialize_tree(vector):
    root = None
    for item in vector:
        root = BSTTree.insert(root, item)
    return root

# Question 2
def print_balances(root):
    if root is None:
        return
    print("Balance factor of node with data", root.data, ":", BSTTree.get_balance(root))
    print_balances(root.left)
    print_balances(root.right)

# Question 3
trees = []
vector = list(range(1000))

for x in range(1000):
    random.shuffle(vector)
    root = initialize_tree(vector)
    trees.append(root)

abs_balances = []
avg_balances = []
balance_test_times = []

def balance_test(root):
    balance_factors = []
    for x in range(len(vector)):
        node = BSTTree.search(vector[x],root)
        balance_factors.append(BSTTree.get_balance(node))
    avg_balances.append(sum(balance_factors) / len(balance_factors))
    abs_balances.append(max(max(balance_factors), -1 * min(balance_factors)))

for root in trees:
    balance_test_times.append(timeit.timeit(lambda: balance_test(root), number=1))

# Question 5
import matplotlib.pyplot as plt

# Plot aided by ChatGPT
plt.figure(figsize=(8, 6))
plt.scatter(abs_balances, balance_test_times, color='blue', alpha=0.7)
plt.xlabel('Absolute Balance')
plt.ylabel('Search Time')
plt.title('Scatterplot of Absolute Balance vs Search Time')
plt.grid(True)
plt.show()


