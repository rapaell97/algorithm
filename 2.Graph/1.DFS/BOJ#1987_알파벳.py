import sys
input = sys.stdin.readline
sys.stdin = open('../../a.txt', 'r')

def dfs(i, k, cnt):
    global ans
    ans = max(cnt, ans)

    for j in range(4):
        ni = i + di[j]
        nk = k + dk[j]

        if 0<= ni <R and 0<= nk <C and V[ord(lst[ni][nk]) - 65] == 0:
            V[ord(lst[ni][nk]) - 65] = 1
            dfs(ni, nk, cnt + 1)
            V[ord(lst[ni][nk]) - 65] = 0

R, C = map(int, input().split())
lst = [list(input()) for _ in range(R)]

di = [-1, 0, 1, 0]
dk = [0, 1, 0, -1]

V = [0] * 26
V[ord(lst[0][0]) - 65] = 1

ans = 0
dfs(0, 0, 0)
print(ans + 1)