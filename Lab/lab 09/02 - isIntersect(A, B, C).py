def isIntersect(a, b, c):
    is_common = False
    for i in a:
        if i in b and i in c:
            is_common = True
            break
    if is_common:
        print("True")
    else:
        print("False")
        
isIntersect(input().split(), input().split(), input().split())

#Big(O) = O(n^2) because it uses a nested loop which it will keep
#iterate over all element from a through out b and c