import sys

sys.stdin = open('../../a.txt', 'r')


def dfs(n, i, k):
    ans[n] = lst[i][k]

    if n == 6:
        temp = ''.join(map(str, ans))
        ans_set.add(temp)
        return

    for j in range(4):
        ni = i + di[j]
        nk = k + dk[j]

        if 0 <= ni < 4 and 0 <= nk < 4:
            dfs(n + 1, ni, nk)


T = int(input())
for tc in range(1, T + 1):
    lst = [list(map(int, input().split())) for _ in range(4)]
    di = [-1, 0, 1, 0]
    dk = [0, 1, 0, -1]

    ans_set = set()
    ans = [0] * 7
    for i in range(4):
        for k in range(4):
            dfs(0, i, k)

    print(f"#{tc} {len(ans_set)}")
