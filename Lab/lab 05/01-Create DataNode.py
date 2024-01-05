"""Lab 05.01 - Create DataNode"""
class DataNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, data):
        self.data = data
    
    def set_next(self, next):
        self.next = next

pNew = DataNode(input(), None)
print(pNew.data)
print(pNew.next)
