N, X = map(int, input().split())
lst = list(map(int, input().split()))

ans, temp = sum(lst[:X]), sum(lst[:X])
cnt = 1

for i in range(X, N):
    temp += lst[i]
    temp -= lst[i-X]

    if temp == ans:
        cnt += 1

    if temp > ans:
        ans = temp
        cnt = 1

if ans == 0:
    print('SAD')
else:
    print(ans)
    print(cnt)