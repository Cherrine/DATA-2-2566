"""Exercise 01.04 - Bangna Trad"""
def main(kms):
    """main"""
    if kms >= 0 and kms <= 5.032:
        print("Bangkok")
    elif kms >= 5.032 and kms <= 35.477:
        print("Samut Prakarn")
    elif kms >= 35.477 and kms <= 52.900:
        print("Chachoengsao")
    elif kms >= 52.900 and kms <= 58.855:
        print("Chon Buri")
    else:
        print("InValid")
main(float(input()))
