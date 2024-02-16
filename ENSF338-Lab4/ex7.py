import timeit
import matplotlib.pyplot as plt
import numpy as np

# AI used to make Node and LinkedList classes
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_tail(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    def get_size(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count

    def get_element_at_position(self, pos):
        curr = self.head
        count = 0
        while curr:
            if count == pos:
                return curr.data
            count += 1
            curr = curr.next
        return None
    
    def display(self):
        elements = []
        currNode = self.head
        while currNode:
            elements.append(currNode.data)
            currNode = currNode.next
        return elements

    # Original reverse() implementation
    def reverse(self):
        newhead = None
        prevNode = None
        for i in range(self.get_size()-1, -1, -1):
            currNode = self.get_element_at_pos(i)
            currNewNode = Node(currNode.data)
            if newhead is None:
                newhead = currNewNode
            else:
                prevNode.next = currNewNode
        prevNode = currNewNode
        self.head = newhead

    # ---ex7.2---
    # Optimized reverse() implementation
    def myreverse(self):
        currNode = self.head
        prevNode = None
        while currNode is not None:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
        self.head = prevNode



linkedl = LinkedList()
node1 = Node(1)

elapsed_time_reverse = 0
elapsed_time_myreverse = 0
elapsed_time_reverse.append(timeit.timeit(lambda : linkedl.reverse(), number = 100))
elapsed_time_myreverse.append(timeit.timeit(lambda : linkedl.myreverse(), number = 100))
