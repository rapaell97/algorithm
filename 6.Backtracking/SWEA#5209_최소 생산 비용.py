import sys
sys.stdin = open('../a.txt', 'r')

def dfs(n):
    global result

    if n < N and sum(ans[:n]) > result:
        return

    if n == N:
        result = min(sum(ans), result)
        return

    for j in range(N):
        if V[j] == 0:
            ans[n] = lst[n][j]
            V[j] = 1
            dfs(n+1)
            V[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    V = [0] * N
    ans = [0] * N
    result = 21e8
    dfs(0)

    print(f"#{tc} {result}")