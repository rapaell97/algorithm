from collections import deque
def bfs(start_i, start_k):
    queue = deque()
    queue.append((start_i, start_k))
    while queue:
        i , k = queue.popleft()
        for j in range(4):
            ni = i + di[j]
            nk = k + dk[j]
            if 0<= ni <N and 0<= nk <N and lst[ni][nk] != 1 and visit[ni][nk] == 0:
                visit[ni][nk] = 1
                lst[ni][nk] = lst[i][k]+1
                queue.append((ni, nk))

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = [list(input()) for _ in range(N)]
    for i in range(len(lst)):
        for k in range(len(lst[i])):
            new = int(lst[i][k])
            lst[i][k] = new
    s_i, s_k, e_i, e_k = 0, 0, 0, 0
    di = [-1, 0, 1, 0]
    dk = [0, 1, 0, -1]
    for i in range(N):
        for k in range(N):
            if lst[i][k] == 2:
                s_i = i
                s_k = k
            if lst[i][k] == 3:
                e_i = i
                e_k = k
    visit = [[0 for _ in range(N)] for _ in range(N)]
    bfs(s_i, s_k)

    if visit[e_i][e_k] == 1:
        print(f"#{tc} {lst[e_i][e_k]-3}")
    else:
        print(f"#{tc} {0}")


