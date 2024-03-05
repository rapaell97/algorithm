import sys
sys.stdin = open('../a.txt', 'r')

N = int(input())
lst = list(map(int, input().split()))
M = int(input())

start = 1
end = max(lst)

while start <= end:
    mid = (start + end) // 2

    temp = 0
    for i in lst:
        if i >= mid:
            temp += mid
        else:
            temp += i

    if temp > M:
        end = mid - 1
    else:
        start = mid + 1

print(end)
