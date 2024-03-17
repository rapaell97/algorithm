import sys
sys.stdin = open ('../my_input.txt', 'r')

def dfs(n, temp):
    global ans

    if n == N:
        if temp < ans:
            ans = temp
        return

    for k in range(N):
        if use[k] == 0:
            use[k] = 1
            dfs(n + 1, temp + lst[n][k])
            use[k] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    use = [0] * N

    ans = 10 * N
    dfs(0, 0)
    print(f"#{tc} {ans}")