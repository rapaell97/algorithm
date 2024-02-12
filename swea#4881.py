def dfs(n,temp):
    global ans
    if temp > ans:
        return
    if n == N:
        ans = min(ans,temp)
        return
    for k in range(N):
        if check[k] == 0:
            check[k] = 1
            dfs(n+1,temp+lst[n][k])
            check[k] = 0

T = int(input())
for u in range(1,T+1):
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]
    check = [0 for _ in range(N)]
    ans = 10*N
    dfs(0,0)
    print(f"#{u} {ans}")
