T = int(input())
M = 1000000
lst = [True] * (M + 1)
lst[0], lst[1] = False, False

for i in range(2, int(M ** 0.5)+1):
    if lst[i]:
        for j in range(2*i, M + 1, i):
            if lst[j]:
                lst[j] = False

for _ in range(T):
    N = int(input())
    cnt = 0

    for i in range(2, N//2 + 1):
        if lst[i] and lst[N-i]:
            cnt += 1

    print(cnt)