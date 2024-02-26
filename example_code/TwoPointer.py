# SWEA_퍼펙트 셔플
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(input().split())

    a = 0
    b = (N + 1) // 2

    print(f"#{tc}", end=' ')

    for i in range(N):
        if i % 2 == 0:
            print(lst[a], end=' ')
            a += 1
        else:
            print(lst[b], end=' ')
            b += 1
    print()
