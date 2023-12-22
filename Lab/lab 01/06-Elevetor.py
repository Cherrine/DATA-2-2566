"""Elevator"""
class Elevator:
    """function"""
    def __init__(self, max_floor):
        self.current_floor = 1
        self.max_floor = max_floor

    def go_to_floor(self):
        """go to floor"""
        while True:
            floor = input()
            if floor.lower() == 'done':
                break
            else:
                floor = int(floor)
                if floor <= self.max_floor and floor >= 1:
                    self.current_floor = floor
                else:
                    print("Invalid Floor!")

    def report_current_floor(self):
        """report current floor"""
        print(self.current_floor)


elevator = Elevator(int(input()))  # Create an elevator that can go up to num floors
elevator.go_to_floor()  # Go to a floor
elevator.report_current_floor()  # Report the current floor
