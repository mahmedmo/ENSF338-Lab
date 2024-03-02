import sys

# stack array implementation shown in class
class MyArrayStack:
    def __init__(self):
        self._storage = []
    def push(self, value):
        self._storage.append(value)
    def pop(self):
        # Note that in Python "not <list>" evaluates to True if the list is empty
        if not self._storage:
            return None
        else:
            return self._storage.pop()
    def peek(self):
        if not self._storage:
            return None
        else:
            return self._storage[-1]

# Exercise 1
# Takes in input when ex1.py is run
# Only addition, subtraction, multiplication, and division are allowed.
# Example commands:
#                   python ex1.py '(+ 1 5)'
#                   python ex1.py '(* (+ 1 5) 2)
#                   python ex1.py '(- (* 1 3) (/ 6 (+ 1 2)))
if len(sys.argv) > 1:
    expression = ' '.join(sys.argv[1:])
else:
    print("No input was received.")

# processing data to make it easier to work with
expression = expression.replace("(", "").replace(")", " ) ").replace("'", "")
exp = expression.split()

# creating stack
stack = MyArrayStack()
for x in exp:
    stack.push(x)
stack.pop()     # removes last ')'

def eval(stack):
    e2 = 0
    e1 = 0
    o = 0

    e2 = stack.pop()
    if (e2 == ')'):
        e2 = eval(stack)

    e1 = stack.pop()   
    if (e1 == ')'):
        e1 = eval(stack)

    o = stack.pop()
    
    if (o == '+'):
        return int(e1) + int(e2)
    elif (o == '-'):
        return int(e1) - int(e2)
    elif (o == '*'):
        return int(e1) * int(e2)
    elif (o == '/'):
        return int(e1) / int(e2)
    else:
        return None


result = eval(stack)
print(result)
    
    
    