tc = int(input())
lst = list()
for i in range(tc):
    lst.append(input())
cnt = 0
for i in lst:
    k = 0
    check = True
    while k < len(i)-1:
        if i[k] == i[k+1]:
            k+=1
        else:
            if i[k] in i[k+1:]:
                check = False
                break
            else:
                k += 1

    if check:
        cnt += 1

print(cnt)
