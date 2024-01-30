test = int(input())
for u in range(test):
    sdo = []
    for i in range(9):
        a = list(map(int, input().split()))
        sdo.append(a)

    check = True

    # Rows check
    for i in range(9):
        check = [0 for _ in range(9)]
        for k in range(9):
            check[sdo[i][k] - 1] += 1
        for j in check:
            if j != 1:
                check = False
                break
        if check is False:
            break

    # Columns check
    if check:
        for k in range(9):
            check = [0 for _ in range(9)]
            for i in range(9):
                check[sdo[i][k] - 1] += 1
            for j in check:
                if j != 1:
                    check = False
                    break
            if check is False:
                break

    # 3x3 subgrid check
    if check:
        i = 0
        while i < 9:
            k = 0
            while k < 9:
                check = [0 for _ in range(9)]
                for m in range(i, i + 3):
                    for n in range(k, k + 3):
                        check[sdo[m][n] - 1] += 1
                for j in check:
                    if j != 1:
                        check = False
                        break
                if check is False:
                    break
                k += 3
            if check is False:
                break
            i += 3

    # Output result
    print(1 if check else 0)
