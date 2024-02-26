import sys
sys.stdin = open ('my_input.txt', 'r')
from collections import deque
def dfs(n):
    print(n, end=' ')
    visit[n] = 1

    for j in range(1, N + 1):
        if j in graph[n] and visit[j] == 0:
            dfs(j)

def bfs(n):
    print(n, end=' ')
    visit[n] = 1
    queue = deque()
    queue.append(n)

    while queue:
        temp = queue.popleft()

        for j in range(1 , N + 1):
            if j in graph[temp] and visit[j] == 0:
                visit[j] = 1
                queue.append(j)
                print(j, end=' ')

N , M , V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for i in range(M):
    a , b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [0] * (N + 1)
dfs(V)
print()
visit = [0] * (N + 1)
bfs(V)