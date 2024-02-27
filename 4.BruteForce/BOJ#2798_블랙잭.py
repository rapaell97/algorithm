import sys
sys.stdin = open ('my_input.txt', 'r')
############### dfs 방식 ###############
def dfs(n):
    global ans

    if n == 3:
        if sum(ans_lst) <= M:
            ans = max(ans, sum(ans_lst))
        return

    for j in range(N):
        if use[j] == 0:
            use[j] = 1
            ans_lst[n] = card[j]
            dfs(n + 1)
            use[j] = 0


N, M = map(int, input().split())
card = list(map(int, input().split()))
use = [0] * N
ans_lst = [0] * 3

ans = 0
dfs(0)
print(ans)

############### 3중 for문 방식 ###############
N, M = map(int, input().split())
lst = list(map(int, input().split()))
sum_lst = list()

for i in range(N - 2):
    for k in range(i + 1, N - 1):
        for j in range(k + 1, N):
            check = lst[i] + lst[k] + lst[j]

            if check <= M:
                sum_lst.append(check)

print(max(sum_lst))

