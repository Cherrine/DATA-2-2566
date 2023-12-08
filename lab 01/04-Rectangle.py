"""Rectangle"""
class Rectangle:
    """init"""
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        """area"""
        return self.height * self.width

    def calculate_perimeter(self):
        """perimeter"""
        return 2 * (self.height + self.width)

def calculate():
    """calculate"""
    rectangle = Rectangle(float(input()), float(input()))
    condition = input()
    if condition == "area":
        result = rectangle.calculate_area()
    else:
        result = rectangle.calculate_perimeter()
    print("%.2f" % result)

calculate()
