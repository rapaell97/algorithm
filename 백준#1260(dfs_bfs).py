from collections import deque
v, e, start = map(int,input().split())
visit_dfs = [0 for _ in range(v+1)]
visit_bfs = [0 for _ in range(v+1)]
ans_dfs = list()
ans_bfs = list()
graph = [[] for _ in range(v+1)]
for i in range(e):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(v+1):
    graph[i].sort()

def dfs(node):
    visit_dfs[node] = 1
    ans_dfs.append(node)
    for i in graph[node]:
        if visit_dfs[i] == 0:
            dfs(i)

def bfs_queue(node):
    queue = deque([node])
    visit_bfs[node] = 1
    while queue:
        now = queue.popleft()
        ans_bfs.append(now)
        for i in graph[now]:
            if visit_bfs[i] == 0:
                visit_bfs[i] = 1
                queue.append(i)

dfs(start)
bfs_queue(start)
print(*ans_dfs)
print(*ans_bfs)
