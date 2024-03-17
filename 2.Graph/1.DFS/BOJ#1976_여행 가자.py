import sys
input = sys.stdin.readline
def dfs(n):
    for j in graph[n]:
        if visit[j] == 0:
            visit[j] = 1
            dfs(j)

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
visit = [0] * (N + 1)

for i in range(1, N + 1):
    temp = list(map(int, input().split()))

    for j in range(len(temp)):
        graph[i].append(i)
        if temp[j] == 1:
            graph[i].append(j + 1)
            graph[j + 1].append(i)

plan = list(map(int, input().split()))
dfs(plan[0])

check = True
for i in plan:
    if visit[i] == 0:
        check = False
        break

if check:
    print('YES')
else:
    print('NO')