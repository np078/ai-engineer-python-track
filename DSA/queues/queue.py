# Implementing Queue using General method

from collections import deque

class queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, value):
        self.buffer.appendleft(value)

    def dequeue(self):
       return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    
q = queue()
q.enqueue(7)
q.enqueue(9)
q.enqueue(56)
q.enqueue(90)
print(q.dequeue())
print(q.buffer)


