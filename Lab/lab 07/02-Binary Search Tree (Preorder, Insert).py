class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def set_root(self, root):
        self.root = root

    def insert(self, data):
        if self.root is None:
            self.root = BSTNode(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = BSTNode(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = BSTNode(data)
            else:
                self._insert(data, node.right)

    def preorder(self):
        return self._preorder(self.root)

    def _preorder(self, node):
        if node is not None:
            print(f"-> {node.data}", end=" ")
            self._preorder(node.left)
            self._preorder(node.right)

def main():
    my_bst = BST()
    for _ in range(int(input())):
        my_bst.insert(int(input()))

    print("Preorder: ", end="")
    my_bst.preorder()

main()
