import sys
sys.stdin = open ('my_input.txt', 'r')
from collections import deque
def bfs(i, k):
    global distance

    queue = deque()
    queue.append((i, k))
    visit[i][k] = 1

    while queue:

        for _ in range(len(queue)):
            i, k = queue.popleft()
            if i == N - 1 and k == M - 1:
                print(distance)
                return

            for j in range(4):
                ni = i + di[j]
                nk = k + dk[j]

                if 0<= ni <N and 0<= nk <M and visit[ni][nk] == 0 and mirro[ni][nk] == '1':
                    visit[ni][nk] = 1
                    queue.append((ni , nk))

        distance += 1


N , M = map(int, input().split())

mirro = [list(input()) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
di = [-1, 0, 1, 0]
dk = [0, 1, 0, -1]

distance = 1
bfs(0 , 0)


