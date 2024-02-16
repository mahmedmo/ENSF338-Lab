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

def myreverse(self):
    currNode = self.head
    prevNode = None
    while currNode is not None:
        nextNode = currNode.next
        currNode.next = prevNode
        prevNode = currNode
        currNode = nextNode
    self.head = prevNode
