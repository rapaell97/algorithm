v, e = map(int,input().split())
visit = [0 for _ in range(v+1)]
graph = [[0 for _ in range(v+1)] for _ in range(v+1)]
for i in range(e):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(node):
    visit[node] = 1
    for i in range(1,v+1):
        if visit[i] == 0 and graph[node][i] == 1:
            dfs(i)
cnt = 0
for i in range(1,len(visit)):
    if visit[i] == 0:
        dfs(i)
        cnt += 1

print(cnt)