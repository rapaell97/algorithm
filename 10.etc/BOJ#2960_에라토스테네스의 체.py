N, K = map(int, input().split())
lst = [True] * (N + 1)
lst[0], lst[1] = False, False

check = False
ans, cnt = 0, 0
for i in range(2, N+1):
    if lst[i]:
        for j in range(i, N+1, i):
            if lst[j]:
                cnt += 1
                lst[j] = False
                ans = j

            if cnt == K:
                check = True
                print(ans)
                break
    if check:
        break