from collections import deque
def bfs(x,cnt):
    queue = deque()
    queue.append((x, cnt))
    visit[x] = 1
    while queue:
        index, cnt = queue.popleft()
        if index == b:
            return cnt
        for j in graph[index]:
            if not visit[j]:
                visit[j] = 1
                queue.append((j, cnt+1))
    else:
        return -1

n = int(input())
a , b = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visit = [0 for _ in range(n + 1)]
for j in range(m):
    p , q = map(int,input().split())
    graph[p].append(q)
    graph[q].append(p)

print(bfs(a,0))




