import sys
sys.stdin = open('../../a.txt', 'r')
from collections import deque

move = {1: [[-1, 0, 1, 0], [0, 1, 0, -1]],
        2: [[-1, 0, 1, 0], [0, 0, 0, 0]],
        3: [[0, 0, 0, 0], [0, 1, 0, -1]],
        4: [[-1, 0, 0, 0], [0, 1, 0, 0]],
        5: [[0, 0, 1, 0], [0, 1, 0, 0]],
        6: [[0, 0, 1, 0], [0, 0, 0, -1]],
        7: [[-1, 0, 0, 0], [0, 0, 0, -1]],
        }

can_move = [[1, 2, 5, 6], [1, 3, 6, 7], [1, 2, 4, 7], [1, 3, 4, 5]]


def bfs(i, k, X):
    global ans

    queue = deque()
    queue.append((i, k, X))
    time = 1

    while queue:

        for _ in range(len(queue)):
            i, k, X = queue.popleft()

            if time == L:
                return

            for j in range(4):
                ni = i + move[X][0][j]
                nk = k + move[X][1][j]

                if 0 <= ni < N and 0 <= nk < M and V[ni][nk] == 0 and lst[ni][nk] in can_move[j]:
                    V[ni][nk] = 1
                    queue.append((ni, nk, lst[ni][nk]))
                    ans += 1

        time += 1

T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    V = [[0] * M for _ in range(N)]
    V[R][C] = 1

    ans = 1
    bfs(R, C, lst[R][C])
    print(f"#{tc} {ans}")
