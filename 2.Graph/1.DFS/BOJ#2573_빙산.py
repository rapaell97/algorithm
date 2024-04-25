import sys
sys.setrecursionlimit(10 ** 4)

def melt(arr):
    melt_lst = []
    for i in range(N):
        for k in range(M):

            if arr[i][k] != 0:
                temp = 0
                for j in range(4):
                    ni = i + di[j]
                    nk = k + dk[j]

                    if 0 <= ni < N and 0 <= nk < M:
                        if arr[ni][nk] == 0:
                            temp += 1
                if temp > 0:
                    melt_lst.append((i, k, temp))

    for i in range(len(melt_lst)):
        p, q, mel = melt_lst[i]
        arr[p][q] -= mel

        if arr[p][q] < 0:
            arr[p][q] = 0


def dfs(i, k):
    V[i][k] = 1
    for j in range(4):
        ni = i + di[j]
        nk = k + dk[j]

        if 0 <= ni < N and 0 <= nk < M and V[ni][nk] == 0 and lst[ni][nk] != 0:
            dfs(ni, nk)


N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
di = [-1, 0, 1, 0]
dk = [0, 1, 0, -1]

ans = 0
while True:
    cnt = 0
    check = False
    V = [[0] * M for _ in range(N)]
    for i in range(N):
        for k in range(M):
            if lst[i][k] != 0 and V[i][k] == 0:
                check = True
                dfs(i, k)
                cnt += 1

    if cnt >= 2:
        print(ans)
        break

    elif check and cnt < 2:
        melt(lst)
        ans += 1

    if not check:
        print(0)
        break
