import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('../a.txt', 'r')

def dfs(i, k):

    if i == M - 1 and k == N - 1:
        return 1

    if dp[i][k] == -1:
        dp[i][k] = 0

        for j in range(4):
            ni = i + di[j]
            nk = k + dk[j]

            if 0 <= ni < M and 0 <= nk < N and lst[ni][nk] < lst[i][k]:
                 dp[i][k] += dfs(ni, nk)

    return dp[i][k]


M, N = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]

di = [-1, 0, 1, 0]
dk = [0, 1, 0, -1]

print(dfs(0, 0))
