K, N = map(int, input().split())
lst = [int(input()) for _ in range(K)]

S = 1
E = max(lst)
ans = 0

while S <= E:
    mid = (S + E) // 2

    temp = 0
    for i in lst:
        temp += (i // mid)

    if temp >= N:
        ans = mid
        S = mid + 1
    else:
        E = mid - 1

print(ans)