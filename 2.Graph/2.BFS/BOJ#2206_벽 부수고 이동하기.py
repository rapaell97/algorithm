from collections import deque
import sys

input = sys.stdin.readline


def bfs(i, k, chance):
    global ans
    temp = 1
    V = [[[0, 0] for _ in range(M)] for _ in range(N)]
    queue = deque()
    queue.append((i, k, chance))
    V[i][k][1] = 1
    V[i][k][0] = 0
    while queue:

        for _ in range(len(queue)):
            i, k, chance = queue.popleft()

            if i == N - 1 and k == M - 1:
                if temp < ans:
                    ans = temp
                return

            for j in range(4):
                ni = i + di[j]
                nk = k + dk[j]

                if 0 <= ni < N and 0 <= nk < M:
                    if lst[ni][nk] == '0' and V[ni][nk][chance] == 0:
                        V[ni][nk][chance] = 1
                        queue.append((ni, nk, chance))

                    if chance == 1 and lst[ni][nk] == '1':
                        V[ni][nk][0] = 1
                        queue.append((ni, nk, chance - 1))
        temp += 1

    else:
        ans = -1
        return


N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]
di = [-1, 0, 1, 0]
dk = [0, 1, 0, -1]

ans = N * M
bfs(0, 0, 1)
print(ans)
