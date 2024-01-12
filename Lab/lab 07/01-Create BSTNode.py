class BSTNode:
    """function"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def get_data(self):
        """Get data methods"""
        return self.data

    def get_left(self):
        """Get left methods"""
        return self.left

    def get_right(self):
        """Get right methods"""
        return self.right

    def set_data(self, data):
        """Setter methods"""
        self.data = data

    def set_left(self, left):
        """Set left data methods"""
        self.left = left

    def set_right(self, right):
        """Set right data methods"""
        self.right = right

p_new = BSTNode(int(input()))
print(p_new.get_data())
print(p_new.get_left())
print(p_new.get_right())
