v = int(input())
e = int(input())
visit = [0 for _ in range(v+1)]
graph = [[] for _ in range(v+1)]
for i in range(e):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs_stack(com):
    stack = [com]
    while stack:
        now = stack.pop()
        for i in graph[now]:
            if visit[i] == 0:
                stack.append(i)
        visit[now] = 1

dfs_stack(1)
print(visit.count(1)-1)