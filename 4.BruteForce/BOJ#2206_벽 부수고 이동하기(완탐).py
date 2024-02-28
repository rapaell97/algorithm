from collections import deque
import sys
import copy
sys.stdin = open ('../my_input.txt', 'r')
input = sys.stdin.readline

def bfs(i, k):
    global ans
    global temp
    visit = [[0] * M for _ in range(N)]
    queue = deque()
    queue.append((i, k))
    visit[i][k] = 1

    while queue:

        for _ in range(len(queue)):
            i, k = queue.popleft()

            if i == N - 1 and k == M - 1:
                return

            for j in range(4):
                ni = i + di[j]
                nk = k + dk[j]

                if 0<= ni <N and 0<= nk <M and visit[ni][nk] == 0:
                    if lst[ni][nk] == '0':
                        visit[ni][nk] = 1
                        queue.append((ni, nk))
        temp += 1

    else:
        temp = -1
        return

N , M = map(int, input().split())
lst = [list(input()) for _ in range(N)]
di = [-1, 0, 1, 0]
dk = [0, 1, 0, -1]

ans = N * M
fail_lst = []
for i in range(N):
    for k in range(M):
        if lst[i][k] == '1':
            temp = 1

            lst[i][k] = '0'
            bfs(0, 0)
            lst[i][k] = '1'

            if temp != -1 and temp < ans:
                ans = temp
            fail_lst.append(temp)

if max(fail_lst) == -1:
    print(-1)
else:
    print(ans)