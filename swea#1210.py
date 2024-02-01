for _ in range(10):
    case = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]

    i = 0
    k = 0
    ans = 0
    while k < 100:
        if lst[i][k] == 1:
            p = i
            q = k
            result = 0
            while True:
                if q-1 >= 0 and lst[p][q-1] == 1:
                    while True:
                        if q-1 < 0 or lst[p][q-1] == 0:
                            break
                        else:
                            q -= 1
                elif q+1 < 100 and lst[p][q+1] == 1:
                    while True:
                        if q+1 >= 100 or lst[p][q+1] == 0:
                            break
                        else:
                            q += 1
                p += 1
                if p+1 >= 100:
                    result = lst[p][q]
                    break

            if result == 2:
                ans = k
            else:
                k += 1

        if ans == 2:
            break
        else:
            k += 1

    print(f"#{case} {ans}")

