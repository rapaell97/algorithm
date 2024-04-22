import sys

sys.stdin = open('../a.txt', 'r')


def upper_bound(arr, target):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] <= target:
            start = mid + 1
        else:
            end = mid - 1

    return len(arr) - (end + 1)


N, H = map(int, input().split())
J, S = [], []

for i in range(N):
    num = int(input())

    if i % 2 == 0:
        S.append(num)
    else:
        J.append(num)

S.sort()
J.sort()

ans = 21e8
ans_cnt = 0
for i in range(1, H + 1):
    temp_S = upper_bound(S, i - 1)
    temp_J = upper_bound(J, H - i)
    temp = temp_S + temp_J

    if temp < ans:
        ans = temp
        ans_cnt = 1

    elif temp == ans:
        ans_cnt += 1

print(ans, ans_cnt)
