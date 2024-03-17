from collections import deque
import sys
sys.stdin = open ('../my_input.txt', 'r')
def bfs():
    queue = deque()
    global day
    for i in range(N):
        for k in range(M):
            if box[i][k] == 1:
                queue.append((i, k))

    while queue:
        for _ in range(len(queue)):
            i, k = queue.popleft()
            visit[i][k] = 1

            for j in range(4):
                ni = i + di[j]
                nk = k + dk[j]

                if 0<= ni <N and 0<= nk <M and visit[ni][nk] == 0 and box[ni][nk] == 0:
                    visit[ni][nk] = 1
                    queue.append((ni, nk))

        day += 1


M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

visit = [[0] * M for _ in range(N)]
di = [-1, 0, 1, 0]
dk = [0, 1, 0, -1]

day = 0
bfs()

check = True
for i in range(N):
    for k in range(M):
        if box[i][k] != -1 and visit[i][k] == 0:
            check = False
            break
    if not check:
        break

if check:
    print(day - 1)
else:
    print(-1)