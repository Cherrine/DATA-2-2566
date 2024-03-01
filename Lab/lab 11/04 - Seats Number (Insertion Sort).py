"""Labs 11.04 - Seats Number (Insertion Sort)"""
import json as j
def insertionsort(lst, last):
    """Labs 11.04 - Seats Number (Insertion Sort)"""
    #define variable current for checking recent index that is gonna get sorted each time
    cur = 1
    compare = 0

    #keep using while loop til cur = last
    while cur <= last:
        #take the sorted data to be stored at hold
        hold = lst[cur]
        walker = cur - 1
        #loop within while for compare and sort numbers
        while walker >= 0:
            #increase compare value
            compare += 1
            #shift data at walker to the right position
            if is_current_smaller(hold, lst[walker]):
                lst[walker+1] = lst[walker]
                #decrease walker value by 1
                walker -= 1
            else:
                break
        lst[walker+1] = hold
        cur += 1
        print(lst)
    print("Comparison times: {}".format(compare))

def is_current_smaller(current, walker):
    """Check if it's current smaller"""
    if current[0] == walker[0]:
        return int(current[1:]) < int(walker[1:])
    else:
        return current[0] < walker[0]
 
insertionsort(j.loads(input().replace("'", '"')), int(input()))