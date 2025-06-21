class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:       # A class that tracks the head of the linked list
    def __init__(self):
        self.head = None

    def traverse(self):
        current = self.head
        while current:
          print(current.data, end = "-->")
          current = current.next
        print(None)

ll= LinkedList()
ll.head = Node(10)
ll.head.next = Node(30)
ll.head.next.next = Node(40)
ll.traverse()
