import math
def calculator(n):
    total = 0
    for i in range(1, n+1):
        total += math.floor(math.log10(i) + 1)
    total += n-1
    if n != 1:
        total += 1
    print(total)
calculator(int(input()))

#Big(O) = O(n) because it iterates from 1 to n so the time complexity
#is directly value of n and the math.floor and log doesnt affect the
#time complexity