class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:       # A class that tracks the head of the linked list
    def __init__(self):
        self.head = None



def insert_at_position(self, index, data):
        if index < 0:
         print("Invalid position")
         return

        if index == 0:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        current = self.head
        count = 0

        while current is not None and count < index - 1:
            current = current.next
            count += 1

        if current is None:
            print("Index out of bounds")
            return

        new_node.next = current.next
        current.next = new_node
