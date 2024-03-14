import sys
sys.stdin = open('../a.txt', 'r')
N, M = map(int, input().split())
lst = list(map(int, input().split()))

start = 0
end = max(lst)

while start <= end:
    temp = 0
    mid = (start + end) // 2

    for i in lst:
        if i >= mid:
            temp += (i - mid)

    if temp < M:
        end = mid - 1

    elif temp >= M:
        start = mid + 1
        ans = mid

print(ans)
