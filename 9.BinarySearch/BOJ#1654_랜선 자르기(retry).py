K, N = map(int, input().split())
lst = [int(input()) for _ in range(K)]

start = 1
end = max(lst)

while start <= end:
    cnt = 0
    mid = (start + end) // 2

    for i in lst:
        cnt += i // mid

    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)