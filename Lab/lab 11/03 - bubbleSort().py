"""Labs 11.03 - bubbleSort()"""
import json as j
def bubble_sort(lst, last):
    """Labs 11.03 - bubbleSort()"""
    cur, sortted, compare = 0, False, 0

    while cur <= last and not sortted:
        walker = last
        sortted = True

        while walker > cur:
            if lst[walker] < lst[walker - 1]:
                lst[walker], lst[walker - 1] = lst[walker - 1], lst[walker]
                sortted = False
            walker -= 1
            compare += 1

        cur += 1
        print(lst)

    print("Comparison times: {}".format(compare))
bubble_sort(j.loads(input()), int(input()))