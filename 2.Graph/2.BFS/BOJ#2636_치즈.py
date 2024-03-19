import sys
from collections import deque
sys.stdin = open('../../a.txt', 'r')

def bfs(p, q):
    queue = deque()
    origin_p = p
    origin_q = q
    queue.append((p, q))
    V = [[0] * M for _ in range(N)]
    V[p][q] = 1

    while queue:
        p, q = queue.popleft()
        if p == 0 or p == N or q == 0 or q == M:
            melting.append((origin_p, origin_q))
            return

        for j in range(4):
            np = p + di[j]
            nq = q + dk[j]

            if 0 <= np < N and 0 <= nq < M and lst[np][nq] == 0 and V[np][nq] == 0:
                queue.append((np, nq))
                V[np][nq] = 1


N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
di = [-1, 0, 1, 0]
dk = [0, 1, 0, -1]

ans = []
time = 0
while True:
    if sum(map(sum, lst)) == 0:
        break
    else:
        ans.append(sum(map(sum, lst)))

    time += 1
    melting = []
    for i in range(N):
        for k in range(M):
            if lst[i][k] == 1:
                bfs(i, k)

    for melt in melting:
        a, b = melt
        lst[a][b] = 0

print(time)
print(ans[-1])



