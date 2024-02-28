T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))

    cnt = 0
    now = K
    check = True
    while now < N:
        if now in charge:
            cnt += 1
        else:
            for i in range(K - 1):
                now -= 1
                if now in charge:
                    check = True
                    cnt += 1
                    break
                else:
                    check = False

        if not check:
            break
        else:
            now += K

    if check:
        print(f"#{tc} {cnt}")
    else:
        print(f"#{tc} {0}")