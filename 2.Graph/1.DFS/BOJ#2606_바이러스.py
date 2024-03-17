import sys
sys.stdin = open ('../my_input.txt', 'r')

def dfs(x):
    global ans
    visit[x] = 1

    for j in range(1 , N + 1):
        if j in graph[x] and visit[j] == 0:
            ans += 1
            dfs(j)

N = int(input())
V = int(input())

graph = [[] for _ in range(N + 1)]
visit = [0] * (N + 1)

for i in range(V):
    a , b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

ans = 0
dfs(1)
print(ans)



