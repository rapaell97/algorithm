def dfs(n, cnt):
    global ans

    if n == b:
        ans = cnt
    for j in graph[n]:
        if V[j] == 0:
            V[j] = 1
            dfs(j, cnt+1)

N = int(input())
a, b = map(int, input().split())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    p, q = map(int, input().split())
    graph[p].append(q)
    graph[q].append(p)

V = [0] * (N+1)
ans = 0
dfs(a, 0)

if V[b] == 1:
    print(ans)
else:
    print(-1)