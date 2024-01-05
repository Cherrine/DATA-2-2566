"""Lab02.03"""
class ArrayStack:
    """Class"""
    def __init__(self, lst) -> None:
        """initial"""
        self.lst = lst
 
    def is_empty(self):
        """is_empty"""
        if self.lst == []:
            return True
        else:
            return False
 
    def pop(self):
        """Popping"""
        if self.lst == []:
            print("Underflow: Cannot pop data from an empty list")
        else:
            data = self.lst[-1]
            self.lst.pop()
            return data
 
    def print_stack(self):
        """Printing"""
        return self.lst
  
    def push(self, data):
        """Push"""
        self.lst.append(data)
  
    def size(self):
        """Sizing"""
        return len(self.lst)
  
    def get_stack_top(self):
        """Topping"""
        if self.lst == []:
            return None
        else:
            return self.lst[-1]
 
_NUM_GROUP = int(input())
_NUM_DATA_IN_LIST = int(input())
_ARR = [ArrayStack([]) for _ in range(_NUM_GROUP)]
_LST = [input() for _ in range(_NUM_DATA_IN_LIST)]
_STACK = ArrayStack(_LST)
for i in range(_NUM_DATA_IN_LIST):
    _ARR[i % _NUM_GROUP].push(_STACK.pop())
for i, stack in enumerate(_ARR, start=1):
    print("Group {}: {}".format(str(i), ", ".join(stack.print_stack())))