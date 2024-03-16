import sys
sys.stdin = open ('../my_input.txt', 'r')


def dfs(n):
    global ans
    if n == N:
        temp = 0
        for i in range(N - 1):
            temp += abs(ans_lst[i] - ans_lst[i + 1])

        ans = max(ans, temp)
        return

    for j in range(N):
        if use[j] == 0:
            ans_lst[n] = lst[j]
            use[j] = 1
            dfs(n + 1)
            use[j] = 0


N = int(input())
lst = list(map(int, input().split()))

use = [0] * N
ans_lst = [0] * N

ans = 0
dfs(0)

print(ans)
