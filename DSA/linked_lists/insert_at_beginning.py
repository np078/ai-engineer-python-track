class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def traverse(self):
        current = self.head
        while current:
          print(current.data, end = "-->")
          current = current.next
        print(None)

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

ll = Linkedlist()
ll.head =  Node(6)
ll.head.next = Node(8)
ll.head.next.next = Node(67)
ll.traverse()
ll.insert_at_beginning(9)
ll.traverse()