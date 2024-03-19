import sys
input = sys.stdin.readline

def dfs(n, pre):
    if n == 6:
        print(*ans)
        return

    for i in lst:
        if V[i] == 0 and i > pre:
            V[i] = 1
            ans[n] = i
            dfs(n+1, i)
            V[i] = 0


while True:
    lst = list(map(int, input().split()))
    if lst == [0]:
        break
    lst.pop(0)
    N = len(lst)
    V = [0] * 50
    ans = [0] * 6

    dfs(0, 0)
    print()

