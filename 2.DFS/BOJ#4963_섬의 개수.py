import sys
sys.stdin = open ('../my_input.txt', 'r')

di = [-1, -1, -1, 0, 0, 1, 1, 1]
dk = [-1, 0, 1, -1, 1, -1, 0, 1]
def dfs(i, k):
    lst[i][k] = 0

    for j in range(8):
        ni = i + di[j]
        nk = k + dk[j]

        if 0<= ni <h and 0<= nk <w and lst[ni][nk] == '1':
            dfs(ni, nk)

while True:
    w , h = map(int, input().split())
    if w == 0 and h == 0:
        break

    lst = [list(input().split()) for _ in range(h)]

    ans = 0
    for i in range(h):
        for k in range(w):
            if lst[i][k] == '1':
                dfs(i, k)
                ans += 1

    print(ans)