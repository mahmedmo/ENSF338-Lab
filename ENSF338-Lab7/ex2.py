class Node:
    def __init__(self, data, left=None, right=None, height=1):
        self.data = data
        self.left = left
        self.right = right
        self.height = height

class BSTTree(object):
    def insert(self, root, data):
        path = []
        root = self.insert_helper(root, data, path)
        
        pivot_index = self.find_pivot_index(path)
        if pivot_index == -1:  
            print("Case 1: Pivot not detected.")
            self.adjust_balances(path, 0, len(path), data)
        else:
            pivot = path[pivot_index]
            if ((self.get_balance(pivot) == 1 and data < pivot.data) or
                (self.get_balance(pivot) == -1 and data > pivot.data)):  
                print("Case 2: A pivot exists, and a node was added to the shorter subtree.")
                self.adjust_balances(path, pivot_index, len(path), data)
            else:  
                print("Case 3: Not supported.")

        return root
    
    def insert_helper(self, node, data, path):
        if not node:
            return Node(data)
        elif data < node.data:
            path.append(node)
            node.left = self.insert_helper(node.left, data, path)
        else:
            path.append(node)
            node.right = self.insert_helper(node.right, data, path)
        
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        return node

    def find_pivot_index(self, path):
        for i in reversed(range(len(path))):
            if self.get_balance(path[i]) != 0:
                return i
        return -1

    def adjust_balances(self, path, start, end, data):
        for i in range(start, end):
            if data < path[i].data:
                path[i].height -= 1  
            else:
                path[i].height += 1

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
        print(f"{root.data} ", end="")
        self.pre_order(root.left)
        self.pre_order(root.right)

tree = BSTTree()
root = None
# Test cases aided with ChatGPT
print("TESTING CASE 1...")
root = tree.insert(root, 3)  
print("TESTING CASE 1 DONE...\n")
print("TESTING CASE 2...")
root = tree.insert(root, 1)  
print("TESTING CASE 2 DONE...\n") 
print("TESTING CASE 3...")
root = tree.insert(root, 5) 
root = tree.insert(root, 2)  
root = tree.insert(root, 4)  
root = tree.insert(root, 6)  
print("TESTING CASE 3 DONE...\n")

