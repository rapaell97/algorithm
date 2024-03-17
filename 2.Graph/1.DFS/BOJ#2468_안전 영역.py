import sys
sys.stdin = open ('../my_input.txt', 'r')
def dfs(i , k, rain):
    visit[i][k] = 1

    for j in range(4):
        ni = i + di[j]
        nk = k + dk[j]

        if 0<= ni <N and 0<= nk <N and visit[ni][nk] == 0 and lst[ni][nk] > rain:
            dfs(ni, nk, rain)

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
rain_range = max(map(max, lst))

di = [-1, 0, 1, 0]
dk = [0, 1, 0, -1]
ans_lst = list()
for rain in range(rain_range + 1):
    temp = 0
    visit = [[0] * N for _ in range(N)]

    for i in range(N):
        for k in range(N):
            if lst[i][k] > rain and visit[i][k] == 0:
                temp += 1
                dfs(i, k, rain)

    ans_lst.append(temp)

print(max(ans_lst))