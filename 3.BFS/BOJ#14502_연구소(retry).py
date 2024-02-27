import sys
sys.stdin = open ('../my_input.txt', 'r')
import copy
from collections import deque
input = sys.stdin.readline

N , M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
di = [-1, 0, 1, 0]
dk = [0, 1, 0, -1]

def make_wall(x):
    if x == 3:
        bfs()
        return

    for i in range(N):
        for k in range(M):
            if lst[i][k] == 0:
                lst[i][k] = 1
                make_wall(x + 1)
                lst[i][k] = 0

def bfs():
    global ans
    sample_lst = copy.deepcopy(lst)
    queue = deque()

    for i in range(N):
        for k in range(M):
            if sample_lst[i][k] == 2:
                queue.append((i, k))

    while queue:
        p, q = queue.popleft()

        for j in range(4):
            np = p + di[j]
            nq = q + dk[j]

            if 0<= np <N and 0<= nq <M and sample_lst[np][nq] == 0:
                sample_lst[np][nq] = 2
                queue.append((np, nq))

    temp = 0
    for i in range(N):
        for k in range(M):
            if sample_lst[i][k] == 0:
                temp += 1

    ans = max(temp, ans)

ans = 0
make_wall(0)
print(ans)