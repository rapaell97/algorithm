def dfs(x):
    visit[x] = 1
    for j in range(1, N + 1):
        if graph[x][j] == 1 and visit[j] == 0:
            dfs(j)

N , M = map(int, input().split())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(M):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

visit = [0 for _ in range(N+1)]

ans = 0
for i in range(1, N + 1):
    if visit[i] == 0:
        dfs(i)
        ans += 1

print(ans)