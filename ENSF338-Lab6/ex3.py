import sys

if (len(sys.argv)>1):
    expression = sys.argv[1]
else:
    print("No input was received.")


class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None

def construct_tree(postfix):
    stack = []
    for char in postfix:
        if type(char) is not str or not char in ['+', '-', '*', '/']:
            node = Node(char)
            stack.append(node)
        else:
            node = Node(char)
            node1 = stack.pop()
            node2 = stack.pop()
            node.right = node1
            node.left = node2
            stack.append(node)
    t = stack.pop()
    return t

def postfix(expression):    # makes it easier to work with
    stack = []
    output = []
    number = ''
    for character in expression:
        if character.isdigit():
            number += character
        else:
            if number:
                output.append(int(number))
                number = ''
            if character in ['+', '-', '*', '/']:
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.append(character)
            elif character == '(':
                stack.append(character)
            elif character == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
    if number:
        output.append(int(number))
    while stack:
        output.append(stack.pop())
    return output

def calculate(node):
    if node is not None:
        if type(node.value) is int:
            return node.value
        else:
            left_value = calculate(node.left)       # Post-order Traversal for computing result
            right_value = calculate(node.right)
            if node.value == '+':
                return left_value + right_value
            elif node.value == '-':
                return left_value - right_value
            elif node.value == '*':
                return left_value * right_value
            elif node.value == '/':
                return int(left_value / right_value)


postfix_exp = postfix(expression)
tree = construct_tree(postfix_exp)
print(calculate(tree))
