T = int(input())
lst = []
for _ in range(T):
    lst.append(int(input()))

M = max(lst)
arr = [True] * (M+1)
arr[0], arr[1] = False, False

for i in range(2, M+1):
    if arr[i]:
        for j in range(2*i, M+1, i):
            if arr[j]:
                arr[j] = False

for i in lst:
    ans = 0
    for p in range(M+1):
        if arr[p]:
            q = i - p
            if q >= p and arr[q]:
                ans = p

    print(ans, i-ans)








