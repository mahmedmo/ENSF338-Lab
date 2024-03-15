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
