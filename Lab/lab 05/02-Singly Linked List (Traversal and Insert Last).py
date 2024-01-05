"""Lab 05.02 - Singly Linked List (Traversal and Insert Last)"""
class DataNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None

    def traverse(self):
        if not self.head:
            print("This is an empty list.")
        else:
            current = self.head
            while current.get_next():
                print(current.get_data(), end=" -> ")
                current = current.get_next()
            print(current.get_data())

    def insert_last(self, data):
        new_node = DataNode(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.get_next():
                current = current.get_next()
            current.set_next(new_node)
        self.count += 1

    def insert_front(self, data):
        new_node = DataNode(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def insert_before(self, target_data, data):
        new_node = DataNode(data)
        if not self.head:
            print("Cannot insert, " + target_data + " does not exist.")
            return

        current = self.head
        prev = None
        while current and current.get_data() != target_data:
            prev = current
            current = current.get_next()

        if not current:
            print("Cannot insert, " + target_data + " does not exist.")
        else:
            new_node.set_next(current)
            if prev:
                prev.set_next(new_node)
            else:
                self.head = new_node
            self.count += 1

    def delete(self, target_data):
        if not self.head:
            print("Cannot delete, " + target_data + " does not exist.")
            return

        current = self.head
        prev = None
        while current and current.get_data() != target_data:
            prev = current
            current = current.get_next()

        if not current:
            print("Cannot delete, " + target_data + " does not exist.")
        else:
            if prev:
                prev.set_next(current.get_next())
            else:
                self.head = current.get_next()
            self.count -= 1


def main():
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        mylist.insert_last(input())
    mylist.traverse()


main()

