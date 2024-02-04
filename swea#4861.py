def check(arr,n,m):
    for i in range(n):
        for k in range(n-m+1):
            temp = arr[i][k:k+m]
            if temp[::-1] == temp:
                return ''.join(temp)
    for k in range(n):
        for i in range(n-m+1):
            stemp = list()
            for j in range(m):
                stemp.append(lst[i+j][k])
            if stemp == stemp[::-1]:
                return ''.join(stemp)

test = int(input())
for u in range(test):
    n,m = map(int,input().split())
    lst = [list(input()) for _ in range(n)]
    print(f"#{u+1} {check(lst,n,m)}")
