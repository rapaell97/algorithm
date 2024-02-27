import sys
sys.stdin = open ('../my_input.txt', 'r')

def dfs(n, i, temp):
    global ans

    if n == N:
        ans = min(temp + graph[i][0], ans)
        return

    for j in range(1, N):
        if visit[j] == 0:
            visit[j] = 1
            dfs(n + 1, j, temp + graph[i][j])
            visit[j] = 0


T = int(input())
for tc in range(1, T + 1):

    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * N

    ans = 21e8
    dfs(1, 0, 0)
    print(f"#{tc} {ans}")