"""point"""
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def calculate_distance(self, other_point):
        return ((other_point.x - self.x)**2 + (other_point.y - self.y)**2) ** 0.5

def calculate():
    x1 = float(input())
    y1 = float(input())
    point1 = Point(x1, y1)

    x2 = float(input())
    y2 = float(input())
    point2 = Point(x2, y2)

    print("%.2f" %point1.calculate_distance(point2))
calculate()
