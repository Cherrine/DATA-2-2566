"""is_even"""
def iseven(num):
    """num check"""
    numstr = str(num)
    if len(numstr) == 1:
        if numstr in ["2", "4", "6", "8", "10"]:
            print("True")
        else:
            print("False")
    else:
        num = str(num)[-1]
        if num in ["1", "3", "5", "7", "9"]:
            print("False")
        else:
            print("True")
iseven(int(input()))
