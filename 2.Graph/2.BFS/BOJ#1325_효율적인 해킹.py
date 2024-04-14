import sys
input = sys.stdin.readline
from collections import deque


def bfs(n):
    global temp
    V = [0] * (N + 1)
    V[n] = 1
    queue = deque()
    queue.append(n)

    while queue:
        com = queue.popleft()

        for next in graph[com]:
            if V[next] == 0:
                V[next] = 1
                queue.append(next)
                temp += 1


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

ans = 0
ans_lst = []
for i in range(1, N + 1):
    temp = 1
    bfs(i)
    if temp > ans:
        ans_lst = [i]
        ans = temp

    elif temp == ans:
        ans_lst.append(i)

print(*ans_lst)
