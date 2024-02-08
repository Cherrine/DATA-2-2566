"""Exercise 00.03 - Sorting Name (Sorting)"""
def partition(arr, low, high):
    """Partitions the given array around a pivot element."""
    iii = (low - 1)
    pivot = arr[high]
    if high >= 0:
        for jjj in range(low, high):
            if arr[jjj] <= pivot:
                iii = iii + 1
                arr[iii], arr[jjj] = arr[jjj], arr[iii]

        arr[iii + 1], arr[high] = arr[high], arr[iii + 1]
        return iii + 1
    else:
        return low

def quick_srt(arr, lll, hhh):
    """Performs quicksort on the given array."""
    size = hhh - lll + 1

    if size <= 1:
        return

    stack = [-1] * (size)
    top = -1
    top += 1
    stack[top] = lll
    top += 1
    stack[top] = hhh
    while top >= 0:
        hhh = stack[top]
        top -= 1
        lll = stack[top]
        top -= 1
        ppp = partition(arr, lll, hhh)
        if ppp - 1 > lll:
            top += 1
            stack[top] = lll
            top += 1
            stack[top] = ppp - 1
        if ppp + 1 < hhh:
            top += 1
            stack[top] = ppp + 1
            top += 1
            stack[top] = hhh


def srt_names():
    """Reads a list of names from the user, sorts them using quicksort, and prints them."""
    num_names = int(input())
    names = []
    if num_names <= 0:
        return
    for _ in range(num_names):
        name = input()
        names.append(name)
    quick_srt(names, 0, len(names)-1)
    for name in names:
        print(name)

srt_names()
