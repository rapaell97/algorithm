lst = [4,4,5,7,8,10,20,22,23,24]
n = int(input())
s = 0
e = len(lst) - 1
check = False

while s <= e:
    m = (s+e)//2
    if lst[m] == n:
        check = True
        break
    elif lst[m] < n:
        s = m + 1
    else:
        e = m - 1
if check:
    print("O")
else:
    print("X")




