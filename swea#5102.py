from collections import deque
def bfs(S,cnt):
    queue = deque()
    queue.append((S,cnt))
    while queue:
        now , cnt = queue.popleft()
        visit[now] = 1
        if now == G:
            return cnt
        for j in range(len(visit)):
            if graph[now][j] != 0 and visit[j] == 0:
                visit[j] = 1
                queue.append((j,cnt+1))
    else:
        return 0

T = int(input())
for tc in range(1,T+1):
    V , E = map(int,input().split())

    graph = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for i in range(E):
        a , b = map(int,input().split())
        graph[a][b] = 1
        graph[b][a] = 1

    S,G = map(int,input().split())

    visit = [0 for _ in range(V+1)]
    print(f"#{tc}",bfs(S,0))



