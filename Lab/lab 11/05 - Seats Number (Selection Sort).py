"""Labs 11.05 - Seats Number (Selection Sort)"""
import json as j
def selection_sort(lst, last):
    """Labs 11.05 - Seats Number (Selection Sort)"""
    cur = 0
    compare = 0

    while cur < last:
        smallest = cur
        walker = cur + 1
 
        while walker <= last:
            # เปรียบเทียบค่าของ walker กับค่าของ smallest
            if is_walker_smaller(lst[walker], lst[smallest]):
                smallest = walker
            walker += 1
            compare += 1
 
        # สลับค่าของ elements ที่ current และ smallest
        lst[cur], lst[smallest] = lst[smallest], lst[cur]
        cur += 1
        print(lst)

    print("Comparison times: {}".format(compare))
def is_walker_smaller(walker, smallest):
    """Check if it's smallest"""
    if walker[0] == smallest[0]:
        return int(walker[1:]) < int(smallest[1:])
    else:
        return walker[0] < smallest[0]

selection_sort(j.loads(input().replace("'", '"')), int(input()))