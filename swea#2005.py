test = int(input())
for u in range(test):
    num = int(input())
    lst = [[0 for _ in range(num)]for _ in range(num)]
    for i in range(len(lst)):
        lst[i][0] = 1
    for i in range(1,len(lst)):
        for k in range(1,len(lst[i])):
            lst[i][k] = lst[i-1][k-1]+lst[i-1][k]

    print(f"#{u+1}")
    for i in range(len(lst)):
        for k in range(len(lst[i])):
            if lst[i][k] != 0:
                print(lst[i][k],end=' ')
        print()




