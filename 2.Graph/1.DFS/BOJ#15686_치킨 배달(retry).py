import sys
sys.stdin = open('../../a.txt', 'r')

def cal(arr):
    temp_ans = 0
    for hi, hk in home:
        temp = 21e8
        for ci, ck in arr:
            temp = min(temp, abs(hi - ci) + abs(hk - ck))
        temp_ans += temp

    return temp_ans


def dfs(n, arr):
    global ans

    if n == S:
        if len(arr) == M:
            ans = min(ans, cal(arr))
        return

    dfs(n+1, arr+[chicken[n]])
    dfs(n+1, arr)

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

home, chicken = [], []
for i in range(N):
    for k in range(N):
        if city[i][k] == 1:
            home.append((i, k))
        elif city[i][k] == 2:
            chicken.append((i, k))

S = len(chicken)

ans = 21e8
temp_lst = []
dfs(0, temp_lst)
print(ans)


