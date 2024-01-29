test = int(input())

for u in range(test):

    galo = int(input())
    lst = [[0 for _ in range(101)] for _ in range(galo)]
    height = list(map(int,input().split()))

    for i in range(len(height)):
        for k in range(height[i]):
            lst[i][k]=1

    #print(lst)
    drop=[0 for _ in range(101)]

    for k in range(101):
        for i in range(len(lst)):
            if lst[i][k] == 1:
                for p in range(i+1,len(lst)):
                    if lst[p][k]==0:
                        drop[k]+=1
            break

    print(f"#{u+1} {max(drop)}")




