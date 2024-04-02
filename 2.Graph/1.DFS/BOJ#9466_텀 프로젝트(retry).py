import sys
sys.setrecursionlimit(10**6)

def dfs(i):
    global ans
    temp.append(i)
    V[i] = 1
    next = lst[i]

    if V[next]:
        if next in temp:
            ans += temp[temp.index(next):]
        return
    else:
        dfs(next)


T = int(input())
for tc in range(T):
    N = int(input())
    lst = [0] + list(map(int, input().split()))
    V = [0] * (N + 1)
    ans = []

    for i in range(1, N + 1):
        if not V[i]:
            temp = []
            dfs(i)
    print(ans)
    print(N - len(ans))
