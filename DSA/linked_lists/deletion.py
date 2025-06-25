class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next

    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None
            
    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty")
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != value:
            current = current.next
        if current.next is None:
            print("Value not found")
            return
        current.next = current.next.next
    
    def display_list(self):
        current = self.head
        while current:
            print(current.data, end="-->")
            current = current.next
        print(None)
        
ll = Linkedlist()
ll.head = Node(5)
ll.head.next = Node(3)
ll.head.next.next = Node(6)
ll.display_list()
ll.delete_by_value(3)
ll.display_list()
