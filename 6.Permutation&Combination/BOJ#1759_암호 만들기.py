import sys
sys.stdin = open('../a.txt', 'r')
input = sys.stdin.readline
def dfs(n, start):
    if n == L:
        temp = 0
        for i in ans:
            if i in mo:
                temp += 1
            if temp > L - 2:
                break

        if 1<= temp <= L - 2:
            print(''.join(ans))
        return

    for j in range(start, C):
        if use[j] == 0:
            use[j] = 1
            ans[n] = arr[j]
            dfs(n + 1, j + 1)
            use[j] = 0


L, C = map(int, input().split())
arr = list(input().split())
arr.sort()
use = [0] * C
ans = [0] * L
mo = ['a', 'e', 'i', 'o', 'u']

dfs(0, 0)