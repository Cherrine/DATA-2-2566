"""Labs 11.06 - Seats Number (Bubble Sort)"""
import json as j
def bubble_sort(lst, last):
    """Labs 11.06 - Seats Number (Bubble Sort)"""
    cur, sortted, compare = 0, False, 0

    while cur <= last and not sortted:
        walker = last
        sortted = True

        while walker > cur:
            letter, num = lst[walker][0], int(lst[walker][1:])
            letter_prev, num_prev = lst[walker - 1][0], int(lst[walker - 1][1:])
            if letter < letter_prev or (letter == letter_prev and num < num_prev):
                lst[walker], lst[walker - 1] = lst[walker - 1], lst[walker]
                sortted = False
            walker -= 1
            compare += 1

        cur += 1
        print(lst)

    print("Comparison times: {}".format(compare))
bubble_sort(j.loads(input().replace("'", '"')), int(input()))