"""Lab 02.01 - Stack (Create Stack)"""
class ArrayStack:
    """stack"""
    def __init__(self):
        self.size = 0
        self.data = []

    def push(self, input_data):
        """Stack"""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1

    def pop(self):
        """pop item"""
        if not self.is_empty():
            return self.data.pop()
        else:
            print("Underflow: Cannot pop data from an empty list")
            return None

    def is_empty(self):
        """if the stack is empty"""
        if self.data == []:
            return True
        else:
            return False

    def get_stack_top(self):
        """get stack stop"""
        if not self.is_empty():
            return self.data[-1]
        else:
            print("Underflow: Cannot get stack top from an empty list")
            return None

    def get_size(self):
        """stack size"""
        return len(self.data)

    def print_stack(self):
        """print stack"""
        print(self.data)
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
