"""main"""
import json
def main():
    """function"""
    my_list = json.loads(input())
    lmx = my_list[0]
    lmn = my_list[0]
    for i in my_list:
        if i < lmn:
            lmn = i
        elif i > lmx:
            lmx = i
    avg = round(sum(my_list) / len(my_list), 2)
    print("(%s, %s, %s)" %(lmx, lmn, avg))
main()
