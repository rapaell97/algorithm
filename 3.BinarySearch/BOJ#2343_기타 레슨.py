N, M = map(int, input().split())
lst = list(map(int, input().split()))

S = max(lst)
E = sum(lst)
ans = 0

while S <= E:
    mid = (S + E) // 2

    temp = 1
    temp_sum = 0
    j = 0

    while j < N:

        if temp_sum + lst[j] <= mid:
            temp_sum += lst[j]

        else:
            temp += 1
            temp_sum = lst[j]

        j += 1

    if temp <= M:
        ans = mid
        E = mid - 1
    else:
        S = mid + 1

print(ans)
