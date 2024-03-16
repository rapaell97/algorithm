import sys
sys.stdin = open ('../my_input.txt', 'r')
def dfs(n):
    global find

    if find:
        return

    if n == 7:
        if sum(ans) == 100:
            ans.sort()
            for j in range(7):
                print(ans[j])
            find = True
        return

    for j in range(9):
        if check[j] == 0:
            check[j] = 1
            ans[n] = lst[j]
            dfs(n + 1)
            check[j] = 0

lst = [int(input()) for _ in range(9)]
check = [0] * 9
ans = [0] * 7
find = False
dfs(0)
