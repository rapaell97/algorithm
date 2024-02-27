from collections import deque
import copy
import sys
sys.stdin = open ('my_input.txt', 'r')
input = sys.stdin.readline

def bfs(i, k, chance):
    global ans
    temp = 1
    V = [[0] * M for _ in range(N)]
    queue = deque()
    queue.append((i, k, chance, V))
    V[i][k] = 1
    while queue:

        for _ in range(len(queue)):
            i, k, chance, V = queue.popleft()

            if i == N - 1 and k == M - 1:
                if temp < ans:
                    ans = temp
                return

            for j in range(4):
                ni = i + di[j]
                nk = k + dk[j]

                if 0<= ni <N and 0<= nk <M and V[ni][nk] == 0:
                    if lst[ni][nk] == '0':
                        V[ni][nk] = 1

                        V2 = copy.deepcopy(V)
                        queue.append((ni, nk, chance, V2))

                    if chance == 1 and lst[ni][nk] == '1':
                        V[ni][nk] = 1

                        V2 = copy.deepcopy(V)
                        queue.append((ni, nk, chance - 1, V2))
        temp += 1

    else:
        ans = -1
        return

N , M = map(int, input().split())
lst = [list(input()) for _ in range(N)]
di = [-1, 0, 1, 0]
dk = [0, 1, 0, -1]

ans = N * M
bfs(0, 0, 1)
print(ans)