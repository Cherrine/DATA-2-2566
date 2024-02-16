def summation(n):
    total = 0
    for i in range(n):
        total += n - i
    print(total)
summation(int(input()))

#Big(O) = O(n) because running time always keep growing 
#with the input size "n"