class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right
        self.balance = 0

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(data, self.root)

    def _insert(self, data, node):
        if node is None:
            return Node(data)

        if data <= node.data:
            node.left = self._insert(data, node.left)
        else:
            node.right = self._insert(data, node.right)

        self.update_balances(node)

        pivot = self.find_pivot(node)
        if pivot is None:
            print("Case #1: Pivot not detected")
        elif abs(pivot.balance) > 1:
            if (data <= pivot.data and pivot.balance > 0) or (data > pivot.data and pivot.balance < 0):
                print("Case #2: A pivot exists, and a node was added to the shorter subtree")
            else:
                print("Case #3: not supported")
                if data <= pivot.data and pivot.left:
                    if data <= pivot.left.data:
                        self._right_rotate(pivot)
        else:
            print("No imbalance after insertion")

        return node

    def update_balances(self, node):
        if node is None:
            return
        while node.parent:
            if node.parent.left == node:
                node.parent.balance += 1
            else:
                node.parent.balance -= 1
            node = node.parent

    def find_pivot(self, node):
        while node:
            if abs(node.balance) > 1:
                return node
            node = node.parent
        return None

    def _right_rotate(self, pivot):
        if pivot.left is None:
            return
        new_root = pivot.left
        pivot.left = new_root.right
        if new_root.right:
            new_root.right.parent = pivot
        new_root.parent = pivot.parent
        if pivot.parent is None:
            self.root = new_root
        elif pivot is pivot.parent.right:
            pivot.parent.right = new_root
        else:
            pivot.parent.left = new_root
        new_root.right = pivot
        pivot.parent = new_root
        # Update balances after rotation
        pivot.balance -= 1 + max(new_root.balance, 0)
        new_root.balance -= 1 - min(pivot.balance, 0)

# Test case to check right rotation
def test_right_rotation():
    tree = AVLTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(2)
    print("Before rotation:")
    print("Root:", tree.root.data)
    print("Root's left child:", tree.root.left.data)
    print("Left child's left child:", tree.root.left.left.data if tree.root.left.left else None)

    tree._right_rotate(tree.root)

    print("\nAfter rotation:")
    print("Root:", tree.root.data)
    print("Root's right child:", tree.root.right.data)
    print("Right child's left child:", tree.root.right.left.data if tree.root.right.left else None)

test_right_rotation()
