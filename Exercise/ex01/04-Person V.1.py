"""Exercise 00.04 - Person V.1"""
class Person:
    def __init__(self):
        self.name = input()
        self.age = input()

    def get_details(self):
        print("{}, {} years old".format(self.name, self.age))

    def say_hello(self):
        print("Hello, my name is {}!".format(self.name))

display = Person()
display.get_details()
display.say_hello() 
