import sys
sys.stdin = open('../a.txt', 'r')
from collections import deque
def flood(arr):
    flood_lst = []
    for i in range(R):
        for k in range(C):
            if arr[i][k] == '*':
                flood_lst.append([i, k])

    for i in range(len(flood_lst)):
        for j in range(4):
            ni = flood_lst[i][0] + di[j]
            nk = flood_lst[i][1] + dk[j]

            if 0<= ni <R and 0<= nk <C and (lst[ni][nk] == '.' or lst[ni][nk] == 'S'):
                arr[ni][nk] = '*'

def bfs(i, k):
    queue = deque()
    queue.append((i, k))
    time = 0

    while queue:
        flood(lst)
        for _ in range(len(queue)):
            i, k = queue.popleft()

            if i == v_i and k == v_k:
                print(time)
                return

            for j in range(4):
                ni = i + di[j]
                nk = k + dk[j]

                if 0<= ni <R and 0<= nk <C and (lst[ni][nk] == '.' or lst[ni][nk] == 'D'):
                    lst[ni][nk] = 'S'
                    queue.append((ni, nk))

        time += 1

    else:
        print('KAKTUS')

R, C = map(int, input().split())
lst = [list(input()) for _ in range(R)]
di = [-1, 0, 1, 0]
dk = [0, 1, 0, -1]

for i in range(R):
    for k in range(C):
        if lst[i][k] == 'D':
            v_i = i
            v_k = k
        elif lst[i][k] == 'S':
            g_i = i
            g_k = k

bfs(g_i, g_k)
