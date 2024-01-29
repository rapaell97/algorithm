test = int(input())
for i in range(test):
    num = int(input())
    lst = list(map(int,input().split()))
    sell=lst[-1]
    result=0
    for k in lst[-2::-1]:
        if k > sell:
            sell = k
        else:
            result+=sell-k

    print(f"#{i+1} {result}")










