"""Lab 05.02 Singly Linked List"""
class DataNode:
    """Announced Class Datanode"""
    def __init__(self, data=None):
        """Announced Initation"""
        self.__data = data
        self.__next = None
 
    def get_data(self):
        """Announce Self"""
        return self.__data
 
    def set_data(self, data):
        """Announced Data and Self"""
        self.__data = data
 
    def get_next(self):
        """Announce self_next"""
        return self.__next
 
    def set_next(self, next_node):
        """Announce self_next_node"""
        self.__next = next_node
 
class SinglyLinkedList:
    """SinglyLinkedList"""
    def __init__(self) -> None:
        """Self"""
        self.count = 0
        self.head = None
 
    def traverse(self):
        """Important"""
        if self.head is None:
            print("This is an empty list.")
            return
        current = self.head
        while current is not None:
            self.count -= 1
            if self.count == 0:
                print(current.get_data())
                current = current.get_next()
            else:
                print(current.get_data(), end=" -> ")
                current = current.get_next()
 
    def insert_last(self, data):
        """Insert_last"""
        new_node = DataNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)
        self.count += 1
 
    def insert_front(self, data):
        """Insert_front"""
        new_node = DataNode(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1
 
    def insert_before(self, node_data, data):
        """Insert_before"""
        new_node = DataNode(data)
        current = self.head
        previous = None
 
        if current is None:
            print("Cannot insert, {} does not exist.".format(node_data))
            return
 
        if current.get_data() == node_data:
            self.insert_front(data)
            return
 
        while current is not None and current.get_data() != node_data:
            previous = current
            current = current.get_next()
 
        if current is None:
            print("Cannot insert, {} does not exist.".format(node_data))
            return
 
        new_node.set_next(current)
        previous.set_next(new_node)
        self.count += 1
 
    def delete(self, data):
        """Delete"""
        current = self.head
        previous = None
 
        if current is None:
            print("Cannot delete, {} does not exist.".format(data))
            return
 
        if current.get_data() == data:
            self.head = current.get_next()
            self.count -= 1
            return
 
        while current is not None and current.get_data() != data:
            previous = current
            current = current.get_next()
 
        if current is None:
            print("Cannot delete, {} does not exist.".format(data))
            return
 
        previous.set_next(current.get_next())
        self.count -= 1
 
LIST1_ = SinglyLinkedList()
for _ in range(int(input())):
    TEXT_ = input()
    CONDI_, DATA_ = TEXT_.split(": ")
    if CONDI_ == "F":
        LIST1_.insert_front(DATA_)
    elif CONDI_ == "L":
        LIST1_.insert_last(DATA_)
    elif CONDI_ == "B":
        DATA_EXIST, DATA_NEW = DATA_.split(", ")
        LIST1_.insert_before(DATA_EXIST, DATA_NEW)
    elif CONDI_ == "D":
        LIST1_.delete(DATA_)
    else:
        print("Invalid Condition!")
LIST1_.traverse()