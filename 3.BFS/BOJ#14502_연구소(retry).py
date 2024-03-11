import sys
from collections import deque
input = sys.stdin.readline

def bfs(arr):
    V = [[0] * M for _ in range(N)]
    for i, j in arr:
        lst[i][j] = 1
    cnt = S - 3
    queue = deque()
    for vi, vj in virus:
        queue.append((vi, vj))
        V[vi][vj] = 1

    while queue:
        p, q = queue.popleft()

        for j in range(4):
            np = p + di[j]
            nq = q + dk[j]

            if 0<= np <N and 0<= nq <M and lst[np][nq] == 0 and V[np][nq] == 0:
                queue.append((np, nq))
                V[np][nq] = 1
                cnt -= 1

    for i, j in arr:
        lst[i][j] = 0

    return cnt


N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
di = [-1, 0, 1, 0]
dk = [0, 1, 0, -1]

wall_lst = []
virus = []
for i in range(N):
    for k in range(M):
        if lst[i][k] == 0:
            wall_lst.append((i, k))
        elif lst[i][k] == 2:
            virus.append((i, k))

S = len(wall_lst)

ans = 0
for i in range(S-2):
    for j in range(i+1, S-1):
        for k in range(j+1, S):
            ans = max(ans, bfs([wall_lst[i], wall_lst[j], wall_lst[k]]))

print(ans)