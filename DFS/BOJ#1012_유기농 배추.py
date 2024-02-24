import sys
sys.stdin = open ('../my_input.txt', 'r')
sys.setrecursionlimit(10**6)
def dfs(i , k):
    visit[i][k] = 1

    for j in range(4):
        ni = i + di[j]
        nk = k + dk[j]

        if 0<= ni <N and 0<= nk <M and visit[ni][nk] == 0 and graph[ni][nk] == 1:
            dfs(ni , nk)

T = int(input())
for tc in range(T):
    M , N , K = map(int, input().split())

    graph = [[0] * M for _ in range(N)]
    visit = [[0] * M for _ in range(N)]
    di = [-1, 0, 1, 0]
    dk = [0, 1, 0, -1]

    for _ in range(K):
        a , b = map(int, input().split())
        graph[b][a] = 1

    ans = 0
    for i in range(N):
        for k in range(M):
            if graph[i][k] == 1 and visit[i][k] == 0:
                dfs(i , k)
                ans += 1

    print(ans)