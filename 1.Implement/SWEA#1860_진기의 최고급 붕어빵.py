T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arrive = list(map(int, input().split()))
    arrive.sort()
    check = True
    boong = 0
    time = 0
    index = 0
    while index < N:
        if time != 0 and time % M == 0:
            boong += K
        if time == arrive[index]:
            buy = arrive.count(arrive[index])
            boong -= buy
            index += buy
        if boong < 0:
            check = False
            break
        time += 1

    if check:
        print(f"#{tc} Possible")
    else:
        print(f"#{tc} Impossible")
