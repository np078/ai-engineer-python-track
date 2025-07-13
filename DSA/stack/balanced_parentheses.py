# Implemented a balanced parentheses checker using Stack
from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)

    def pop(self):
       return self.container.pop()
    
    def peek(self):
       return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
    
    def __str__(self):
        return f"stack({self.container})"
    
def is_parentheses(expression):
        s = Stack()
        for ch in expression:
            if ch == '(':
                s.push(ch)
            elif ch == ')':
                if s.is_empty():
                    return False
                s.pop()
        return s.is_empty()