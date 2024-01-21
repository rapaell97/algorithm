a,b = input().split()

lst = list()

for i in range(3):
    sub_lst=list()
    for k in range(6):
        if k <=3:
            sub_lst.append(a)
        else:
            sub_lst.append(b)
    lst.append(sub_lst)

for m in lst:
    for n in m:
        print(n,end='')
    print()

