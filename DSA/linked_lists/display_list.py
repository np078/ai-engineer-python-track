class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:       # A class that tracks the head of the linked list
    def __init__(self):
        self.head = None



def print_list(self):
    current = self.head
    while current:
        print(current.data, end = "-->")
        current = current.next
    print(None)