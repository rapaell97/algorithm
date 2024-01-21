lst = list()
for i in range(9):
    h=int(input())
    lst.append(h)

hsum=sum(lst)

for i in range(len(lst)-1):
    if lst.count(-1) == 2:
        break
    for j in range(i+1,len(lst)):
        if hsum-(lst[i]+lst[j]) == 100:
            lst[i] = -1
            lst[j] = -1
            break

lst.sort()

for k in lst:
    if k != -1:
        print(k)

