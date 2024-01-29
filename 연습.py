num = int(input())
lst = [[0 for _ in range(4)]for _ in range(4)]

for i in range(len(lst)):
    if i%2 == 0:
        for k in range(len(lst[i])):
            lst[i][k]=num
            num+=1
    else:
        for k in range(len(lst[i])-1,-1,-1):
            lst[i][k]=num
            num+=1

for i in lst:
    for k in i:
        print(k,end=' ')
    print()
