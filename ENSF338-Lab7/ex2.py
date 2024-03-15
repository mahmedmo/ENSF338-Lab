# Question 1
class Node:
    def __init__(self, data, parent=None, left=None, right=None, balance=0):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right
        self.balance = balance

def insert(data, root=None):
    if root is None:
        return Node(data)

    current = root
    parent = None
    pivot = None

    while current is not None:
        parent = current
        if data <= current.data:
            current = current.left
            if get_balance(current) in (-2, 2):
                pivot = parent
        else:
            current = current.right
            if get_balance(current) in (-2, 2):
                pivot = parent

    newnode = Node(data, parent)
    if data <= parent.data:
        parent.left = newnode
    else:
        parent.right = newnode

    # Update balances along the path to the root
    node = newnode
    while node is not None:
        update_balance(node)
        node = node.parent

    # Check for Case 2 (pivot exists but inserted into a shorter subtree)
    if pivot is not None:
        if (data <= pivot.left.data or pivot.left is None) and pivot.balance == 2:
            print("Case #2: A pivot exists, and a node was added to the shorter subtree")
            return root, pivot  # Rebalancing needed
        elif (data > pivot.right.data or pivot.right is None) and pivot.balance == -2:
            print("Case #2: A pivot exists, and a node was added to the shorter subtree")
            return root, pivot  # Rebalancing needed
    
    # CHECK FOR CASE 3 HERE
    if pivot is not None:
        left_child_bal = get_balance(pivot.left) if pivot.left else 0
        right_child_bal = get_balance(pivot.right) if pivot.right else 0
        
        if pivot.balance == 2 and left_child_bal == -1:
            print("Case 3: A pivot exists with a balance factor of 2, and a node was added causing a left-right imbalance")
            # Perform left-right rotation
            rotate_left(pivot.left)  # First rotate left child right
            rotate_right(pivot)  # Then rotate pivot left
        elif pivot.balance == -2 and right_child_bal == 1:
            print("Case 3: A pivot exists with a balance factor of -2, and a node was added causing a right-left imbalance")
            # Perform right-left rotation
            rotate_right(pivot.right)  # First rotate right child left
            rotate_left(pivot)  # Then rotate pivot right
    # Otherwise, Case 1 or no rebalancing needed
    return root

def rotate_left(node):
    new_root = node.right
    node.right = new_root.left
    if new_root.left:
        new_root.left.parent = node
    new_root.parent = node.parent
    if node.parent is None:  # node is root
        root = new_root
    elif node is node.parent.left:
        node.parent.left = new_root
    else:
        node.parent.right = new_root
    new_root.left = node
    node.parent = new_root

    update_balance(node)
    update_balance(new_root)
    return new_root

def rotate_right(node):
    new_root = node.left
    node.left = new_root.right
    if new_root.right:
        new_root.right.parent = node
    new_root.parent = node.parent
    if node.parent is None:  # node is root
        root = new_root
    elif node is node.parent.right:
        node.parent.right = new_root
    else:
        node.parent.left = new_root
    new_root.right = node
    node.parent = new_root

    update_balance(node)
    update_balance(new_root)
    return new_root

def update_balance(node):
    node.balance = get_balance(node)  # Recalculate balance factor

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

def get_balance(node):
    if node is None:
        return 0  
    return height(node.right) - height(node.left)
def height(node):
    if node is None:
        return 0 
    return 1 + max(height(node.left), height(node.right))