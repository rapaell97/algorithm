def dfs(n,temp):
    global ans
    if n == N:
        if temp >= B:
            ans = min(temp, ans)
        return
    dfs(n+1,temp+lst[n])
    dfs(n+1,temp)

T = int(input())
for tc in range(1,T+1):
    N , B = map(int,input().split())
    lst = list(map(int,input().split()))
    use = [0 for _ in range(N)]
    ans = 10000*N
    dfs(0,0)
    print(f"#{tc} {ans-B}")