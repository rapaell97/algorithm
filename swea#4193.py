from collections import deque
def bfs(i,k,time):
    global ans
    di = [-1,0,1,0]
    dk = [0,1,0,-1]
    visit[i][k] = 1
    queue = deque()
    queue.append((i,k,time))
    while queue:
        p, q, time = queue.popleft()
        if p == g_i and q == g_k:
            if time<ans:
                ans = time
                print(f"#{tc} {ans}")
            return

        for j in range(4):
            ni = p + di[j]
            nk = q + dk[j]
            if 0<= ni <N and 0<= nk <N and visit[ni][nk] == 0 and sea[ni][nk] != 1:
                visit[ni][nk] = 1
                if sea[ni][nk] == 0:
                    queue.append((ni,nk,time+1))
                elif sea[ni][nk] == 2:
                    while True:
                        if time%3 == 2:
                            break
                        time += 1
                    queue.append((ni, nk, time + 1))
    else:
        print(f"#{tc} {-1}")
        return

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    sea = [list(map(int,input().split())) for _ in range(N)]
    visit = [[0 for _ in range(N)] for _ in range(N)]
    s_i , s_k = map(int,input().split())
    g_i , g_k = map(int,input().split())
    ans = N*N
    bfs(s_i,s_k,0)