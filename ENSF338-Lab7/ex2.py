class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right
        self.balance = 0

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

    update_balances(newnode) 

    pivot = find_pivot(newnode) 
    if pivot is None:
        print("Case #1: Pivot not detected")
    elif abs(pivot.balance) > 1:
        if (data <= pivot.data and pivot.balance > 0) or (data > pivot.data and pivot.balance < 0):
            print("Case #2: A pivot exists, and a node was added to the shorter subtree")
        else:
            print("Case #3: not supported")
    else:
        print("No imbalance after insertion")

    return root

def update_balances(node):
    if node is None:
        return
    while node.parent:
        if node.parent.left == node:
            node.parent.balance += 1
        else:
            node.parent.balance -= 1
        node = node.parent

def find_pivot(node):
    while node:
        if abs(node.balance) > 1:
            return node
        node = node.parent
    return None


print("Test Cases:")
root = insert(5)
print("")
insert(3, root) # case 1
insert(4, root) # case 2
insert(1, root) 
insert(8, root) # case 3
print("\n")



