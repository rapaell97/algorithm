test = int(input())
for u in range(test):
    sdo = list()
    for i in range(9):
        a=list(map(int,input().split()))
        sdo.append(a)

    check = True

    for i in range(9):
        check_lst = [0 for _ in range(9)]
        for k in range(9):
            check_lst[sdo[i][k] - 1] += 1
        for j in check_lst:
            if j != 1:
                check = False
                break
        if not check:
            break

        for k in range(9):
            check_lst = [0 for _ in range(9)]
            for i in range(9):
                check_lst[sdo[i][k] - 1] += 1
            for j in check_lst:
                if j != 1:
                    check = False
                    break
            if not check:
                break

        i = 0
        while i < 9:
            k = 0
            while k < 9:
                check_lst = [0 for _ in range(9)]
                for m in range(i,i+3):
                    for n in range(k,k+3):
                        check_lst[sdo[m][n] - 1] += 1
                for j in check_lst:
                    if j != 1:
                        check = False
                        break
                if not check:
                    break
                k += 3
            if not check:
                break
            i += 3

    if check:
        print(f"#{u+1} 1")
    else:
        print(f"#{u+1} 0")






