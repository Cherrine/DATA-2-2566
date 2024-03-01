"""Labs 11.01 - insertionSort()"""
import json as j
def insertion_sort(lst, last):
    """Labs 11.01 - insertionSort()"""
    compare = 0
    current = 1

    while current <= last:
        hold = lst[current]
        walker = current - 1
        while walker >= 0:
            compare += 1
            if hold < lst[walker]:
                lst[walker+1] = lst[walker]
                walker -= 1
            else:
                break
        lst[walker+1] = hold
        current += 1
        print(lst)

    print("Comparison times: {}".format(compare))
insertion_sort(j.loads(input()), int(input()))
