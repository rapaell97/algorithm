from collections import deque
v = int(input())
e = int(input())
visit = [0 for _ in range(v+1)]
graph = [[] for _ in range(v+1)]
for i in range(e):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
def bfs(com):
    queue = deque([com])
    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if visit[next] == 0:
                queue.append(next)
        visit[now] = 1

bfs(1)
print(visit.count(1) - 1)
