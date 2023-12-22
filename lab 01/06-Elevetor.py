"""elevator"""
class Elevator:
    def __init__(self, max_floor):
        self.current_floor = 1
        self.max_floor = max_floor
    
    def go_to_floor(self, floor):
        max_floor = int(input())
        floor = int(input)
        while True:
            if floor <= max_floor:
                pass
                current_floor = floor
            elif floor > max_floor:
                print("Invalid Floor")
            elif floor == "Done":
                print()
    
    def report_current_floor(self):
        print(...)