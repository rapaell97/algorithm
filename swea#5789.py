test = int(input())
for u in range(test):
    n,q = map(int,input().split())
    lst = [0 for _ in range(n)]
    for i in range(1,q+1):
        l,r = map(int,input().split())
        for k in range(n):
            if k+1 in range(l,r+1):
                lst[k] = i

    print(f"#{u+1}",*lst)
