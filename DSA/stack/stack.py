# Creating a stack using collectins module and importing deque class from it

from collections import deque
stack = deque()
stack.append('ww.india.com')
stack.append('ww.china.com')
stack.append('ww.world.com')
stack.append('ww.africa.com')

print(stack.pop())
print(stack)