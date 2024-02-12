from collections import deque
n,m = map(int,input().split())
graph = [list(map(int,input())) for _ in range(n)]
di = [-1,0,1,0]
dk = [0,1,0,-1]
def bfs(i,k):
    queue = deque()
    queue.append((i,k))
    while queue:
        i,k = queue.popleft()
        for j in range(4):
            ni = i + di[j]
            nk = k + dk[j]
            if 0<= ni < n and 0<= nk < m and graph[ni][nk] == 1:
                queue.append((ni,nk))
                graph[ni][nk] = graph[i][k] + 1

bfs(0,0)
print(graph[n-1][m-1])
