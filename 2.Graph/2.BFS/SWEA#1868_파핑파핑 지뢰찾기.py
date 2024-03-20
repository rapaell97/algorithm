import sys

sys.stdin = open('../../a.txt', 'r')
from collections import deque

T = int(input())
di = [-1, -1, 0, 1, 1, 1, 0, -1]
dk = [0, 1, 1, 1, 0, -1, -1, -1]

def around(i, k):
    for j in range(8):
        ni = i + di[j]
        nk = k + dk[j]

        if 0 <= ni < N and 0 <= nk < N and lst[ni][nk] == '*':
            return 0

    return 1


def bfs(i, k):
    queue = deque()
    queue.append((i, k))
    V[i][k] = 1

    while queue:
        i, k = queue.popleft()

        for j in range(8):
            ni = i + di[j]
            nk = k + dk[j]

            if 0 <= ni < N and 0 <= nk < N and lst[ni][nk] == '.' and V[ni][nk] == 0:
                V[ni][nk] = 1

                if around(ni, nk):
                    queue.append((ni, nk))

for tc in range(1, T + 1):
    N = int(input())
    lst = [list(input()) for _ in range(N)]
    V = [[0] * N for _ in range(N)]

    ans = 0
    for i in range(N):
        for k in range(N):

            if lst[i][k] == '.' and V[i][k] == 0 and around(i, k) == 1:
                bfs(i, k)
                ans += 1

    for i in range(N):
        for k in range(N):
            if lst[i][k] == '.' and V[i][k] == 0:
                ans += 1

    print(f"#{tc} {ans}")
