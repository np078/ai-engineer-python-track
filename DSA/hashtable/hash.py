
class Hashtable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 100
    
    def add(self,key,value):
        h = self.get_hash(key)
        self.arr[h] = value
    
    def get(self,key):
        h = self.get_hash(key)
        return self.arr[h]

H = Hashtable()
print(H.get_hash('Naman'))
H.add('Naman',130)
print(H.get('Naman'))
