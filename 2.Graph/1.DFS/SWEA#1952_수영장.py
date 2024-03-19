import sys
sys.stdin = open('../../a.txt', 'r')

def dfs(n, day, month, T_month):
    global ans
    if n > 13:
        return

    if n == 13:
        temp = 0
        temp += (day*price[0] + month*price[1] + T_month*price[2])
        ans = min(temp, ans)
        return

    dfs(n+1, day+plan[n], month, T_month)
    dfs(n+1, day, month+1, T_month)
    dfs(n+3, day, month, T_month+1)



T = int(input())
for tc in range(1, T + 1):
    price = list(map(int, input().split()))
    plan = [0] + list(map(int, input().split()))
    ans = price[3]

    dfs(1, 0, 0, 0)

    print(f"#{tc} {ans}")
