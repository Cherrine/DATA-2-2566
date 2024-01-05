'''class'''
class ArrayStack:
    '''hi'''
    def __init__(self):
        self.size = 0
        self.data = list()
  
    def push(self, data):
        '''push throught'''
        try:
            if data.isdigit():
                data = int(data)
            elif data.replace(".", "", 1).isdigit():
                data = float(data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(data)
            self.size += 1
  
    def pop(self):
        '''poppin'''
        if self.data:
            self.size -= 1
            return self.data.pop(-1)
        else:
            print("Underflow: Cannot pop data from an empty list")
            return None
  
    def is_empty(self):
        '''true or false'''
        return False if self.data else True
  
    def get_stack_top(self):
        '''on -> top'''
        if self.data:
            return self.data[-1]
        else:
            print("Underflow: Cannot get stack top from an empty list")
            return None
  
    def get_size(self):
        '''69'''
        return self.size
  
    def print_stack(self):
        '''big pp'''
        print(self.data)
  
def main(sentense):
    '''()'''
    stats = True
    parantheses = ArrayStack()
    for i in sentense:
        if i == "(":
            parantheses.push("(")
        if i == ')':
            if parantheses.is_empty():
                parantheses.pop()
                stats = False
            else:
                parantheses.pop()
    if not parantheses.is_empty():
        stats = False
    if stats:
        print("Parentheses in {} are matched".format(sentense))
    else:
        print('Parentheses in {} are unmatched'.format(sentense))
    print(stats)
main(input())