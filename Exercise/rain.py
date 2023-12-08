"""rain"""
def rain(types, minutes):
    """function"""
    if types == "Indoor" and minutes >= 480:
        print("True")
    elif types == "Outdoor" and minutes >= 240:
        print("True")
    else:
        print("False")
rain(input(), float(input()))
