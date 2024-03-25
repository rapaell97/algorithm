import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(i, k, cnt):
    global origin_i, origin_k
    global check
    if cnt >= 4:
        for l in range(4):
            check_i = i + di[l]
            check_k = k + dk[l]
            if check_i == origin_i and check_k == origin_k:
                print('Yes')
                exit()
    visit[i][k] = 1

    for j in range(4):
        ni = i + di[j]
        nk = k + dk[j]
        if 0 <= ni < N and 0 <= nk < M and visit[ni][nk] == 0:
            if lst[ni][nk] == lst[i][k]:
                dfs(ni, nk, cnt + 1)
                visit[ni][nk] = 0
    visit[i][k] = 0


N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]
visit = [[0 for _ in range(M)] for _ in range(N)]
di = [-1, 0, 1, 0]
dk = [0, 1, 0, -1]

check = 0
for i in range(N):
    for k in range(M):
        origin_i = i
        origin_k = k
        dfs(i, k, 1)

if check == 0:
    print('No')
