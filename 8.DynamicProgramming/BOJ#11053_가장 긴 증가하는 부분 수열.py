import sys
sys.stdin = open('../a.txt', 'r')

N = int(input())
lst = list(map(int, input().split()))

dp = [0] * N
dp[0] = 1

for i in range(1, N):
    temp = 0
    for j in range(i):
        if lst[j] < lst[i]:
            temp = max(temp, dp[j])
    dp[i] = temp + 1
print(max(dp))

