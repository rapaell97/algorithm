test = int(input())
for u in range(test):
    n, k = list(map(int,input().split()))
    lst = [list(map(int,input().split())) for _ in range(n)]

    ans = 0
    for i in range(n):
        cnt1 = 0
        for j in range(n-1):
            if lst[i][j] == 1:
                cnt1 += 1
                if cnt1 == k:
                    if lst[i][j+1] == 0:
                        ans += 1
                        cnt1 = 0
                elif cnt1 == k-1:
                    if j+1 == n-1 and lst[i][j+1] == 1:
                        ans += 1
            else:
                cnt1 = 0

    for j in range(n):
        cnt1 = 0
        for i in range(n-1):
            if lst[i][j] == 1:
                cnt1 += 1
                if cnt1 == k:
                    if lst[i+1][j] == 0:
                        ans += 1
                        cnt1 = 0
                elif cnt1 == k-1:
                    if i+1 == n-1 and lst[i+1][j] == 1:
                        ans += 1
            else:
                cnt1 = 0

    print(f"#{u+1} {ans}")

