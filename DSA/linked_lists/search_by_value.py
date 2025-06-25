class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Linkedlist:
    def __init__(self):
        self.head = None

    def Search(self,value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False
    
    def display_list(self):
        current = self.head
        while current:
            print(current.data, end="-->")
            current = current.next
        print(None)
    

ll = Linkedlist()
ll.head = Node(7)
ll.head.next = Node(3)
ll.head.next.next = Node(6)
ll.display_list()
print(ll.Search(3))
print(ll.Search(5))