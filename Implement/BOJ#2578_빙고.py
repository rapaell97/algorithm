def bingo(i , k):
    global temp

    if i == 0 and k == 0:
        check_1 = True
        for j in range(5):
            if lst1[i+j][k+j] != lst1[i][k]:
                check_1 = False
                break
        if check_1:
            temp += 1

    elif i == 4 and k == 0:
        check_2 = True
        for r in range(5):
            for c in range(5):
                if r + c == 4:
                    if lst1[r][c] != lst1[i][k]:
                        check_2 = False
                        break
            if not check_2:
                break
        if check_2:
            temp += 1

    if k == 0:
        check_3 = True
        for j in range(5):
            if lst1[i][k + j] != lst1[i][k]:
                check_3 = False
                break
        if check_3:
            temp += 1

    if i == 0:
        check_4 = True
        for j in range(5):
            if lst1[i + j][k] != lst1[i][k]:
                check_4 = False
                break
        if check_4:
            temp += 1

lst1 = [list(map(int, input().split())) for _ in range(5)]
lst2 = [list(map(int, input().split())) for _ in range(5)]

turn = 0
for i in range(5):
    for k in range(5):
        turn += 1

        for p in range(5):
            for q in range(5):
                if lst2[i][k] == lst1[p][q]:
                    lst1[p][q] = 'x'

        temp = 0
        for p in range(5):
            for q in range(5):

                if lst1[p][q] == 'x' and (p == 0 or q == 0):
                    bingo(p, q)

                    if temp >= 3:
                        print(turn)
                        exit()