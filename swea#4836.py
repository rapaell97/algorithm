test = int(input())
for u in range(test):
    lst = [[0 for _ in range(10)] for _ in range(10)]
    case = int(input())
    xylst = list()
    for i in range(case):
        a = list(map(int,input().split()))
        xylst.append(a)

    for c in range(case):
        for i in range(xylst[c][0],xylst[c][2]+1):
            for k in range(xylst[c][1],xylst[c][3]+1):
                lst[i][k] += xylst[c][4]
    cnt = 0
    for i in lst:
        for k in i:
            if k == 3:
                cnt+=1
    print(f"#{u+1} {cnt}")
