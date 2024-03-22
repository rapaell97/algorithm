import sys
sys.stdin = open('../a.txt', 'r')

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
d = [[0] * M for _ in range(N)]
d[0][0] = lst[0][0]

mi = [-1, 0, -1]
mk = [0, -1, -1]
for i in range(N):
    for k in range(M):

        for j in range(3):
            ni = i + mi[j]
            nk = k + mk[j]

            if 0 <= ni < N and 0 <= nk < M:
                d[i][k] = max(d[ni][nk] + lst[i][k], d[i][k])

print(d[N-1][M-1])
