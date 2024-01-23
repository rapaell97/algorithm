test = int(input())
cmd_lst=list()
lst=list()

for i in range(test):
    cmd_lst.append(input().split())

for k in cmd_lst:
    if k[0] == "push":
        lst.append(int(k[1]))
    elif k[0] == "pop":
        if len(lst) == 0:
            print(-1)
        else:
            print(lst.pop())
    elif k[0] == "size":
        print(len(lst))
    elif k[0] == "empty":
        if len(lst) == 0:
            print(1)
        else:
            print(0)
    elif k[0] == "top":
        if len(lst) == 0:
            print(-1)
        else:
            print(lst[-1])
