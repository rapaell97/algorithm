import sys

input = sys.stdin.readline
from collections import deque


def bfs(i, k, c):
    global ans
    temp = 1
    V = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
    V[i][k][c] = 1

    queue = deque()
    queue.append((i, k, c))

    while queue:
        for _ in range(len(queue)):
            i, k, c = queue.popleft()

            if i == N - 1 and k == M - 1:
                if temp < ans:
                    ans = temp
                return

            for j in range(4):
                ni = i + di[j]
                nk = k + dk[j]

                if 0 <= ni < N and 0 <= nk < M:
                    if lst[ni][nk] == '0' and V[ni][nk][c] == 0:
                        V[ni][nk][c] = 1
                        queue.append((ni, nk, c))

                    elif lst[ni][nk] == '1' and c != 0 and V[ni][nk][c] == 0:
                        V[ni][nk][c] = 1
                        queue.append((ni, nk, c - 1))

        temp += 1
    else:
        ans = -1


N, M, K = map(int, input().split())
lst = [list(input()) for _ in range(N)]
di = [-1, 0, 1, 0]
dk = [0, 1, 0, -1]

ans = N * M
bfs(0, 0, K)

print(ans)
