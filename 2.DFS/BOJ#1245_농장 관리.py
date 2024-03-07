import sys
sys.stdin = open('../a.txt', 'r')


def dfs(i, k):
    visit[i][k] = 1

    for j in range(8):
        ni = i + di[j]
        nk = k + dk[j]

        if 0 <= ni < N and 0 <= nk < M and visit[ni][nk] == 0 and lst[ni][nk] <= lst[i][k]:
            dfs(ni, nk)


N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
di = [-1, 0, 1, 0, -1, -1, 1, 1]
dk = [0, 1, 0, -1, -1, 1, -1, 1]

cnt = 0
while True:
    temp = sum(map(sum,visit))
    if temp == N*M:
        break

    mx = -21e8
    for p in range(N):
        for q in range(M):
            if visit[p][q] != 1 and lst[p][q] > mx:
                mx = lst[p][q]
                mx_i = p
                mx_k = q

    if visit[mx_i][mx_k] == 0:
        dfs(mx_i, mx_k)
        cnt += 1

print(cnt)
