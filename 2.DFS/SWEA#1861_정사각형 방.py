import sys
sys.stdin = open ('../my_input.txt', 'r')

def dfs(i, k, cnt):
    global temp

    if cnt > temp:
        temp = cnt

    for j in range(4):
        ni = i + di[j]
        nk = k + dk[j]

        if 0<= ni <N and 0<= nk <N and visit[ni][nk] == 0 and lst[ni][nk] - 1 == lst[i][k]:
            visit[ni][nk] = 1
            dfs(ni, nk, cnt + 1)
            visit[ni][nk] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    di = [-1, 0, 1, 0]
    dk = [0, 1, 0, -1]
    visit = [[0] * N for _ in range(N)]

    mx_cnt = 0
    ans = 0

    for i in range(N):
        for k in range(N):
            temp = 0
            dfs(i, k, 1)

            if temp > mx_cnt:
                mx_cnt = temp
                ans = lst[i][k]
            elif temp == mx_cnt:
                ans = min(ans, lst[i][k])
            else:
                continue

    print(f"#{tc} {ans} {mx_cnt}")

