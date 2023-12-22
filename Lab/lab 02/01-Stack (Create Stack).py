"""Lab 02.01 – Stack (Create Stack)"""
class ArrayStack:
    """stack"""
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        """push item"""
        self.stack.append(item)
    
    def pop(self):
        """pop item"""
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Underflow: Cannot pop data from an empty list")
            return None
    
    def get_stack_top(self):
        """get stack stop"""
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Underflow: Cannot get stack top from an empty list")
            return None
    
    def is_empty(self):
        """if the stack is empty"""
        return len(self.stack) == 0
    
    def get_size(self):
        """stack size"""
        return len(self.stack)
    
    def print_stack(self):
        """print stack"""
        print(self.stack)

STACK_ = ArrayStack()

STACK_.push("100")
STACK_.push(100)
STACK_.push("3.14")
STACK_.push(3.14)
STACK_.push("66.4a")
STACK_.push("Ackerman")

STACK_.print_stack()

print(STACK_.get_size())
VAR1_ = STACK_.pop()
print(VAR1_)
STACK_.print_stack()
print(STACK_.get_size())

while not STACK_.is_empty():
    print(STACK_.pop())
    
print()
print(STACK_.pop())
print(STACK_.get_stack_top())
print(VAR1_)