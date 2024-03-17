T = int(input())
for tc in range(1, T + 1):
    dic = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    DEC = 0
    N, num = input().split()
    num_r = num[::-1]

    for i in range(int(N)):
        if num_r[i] in dic:
            DEC += dic[num_r[i]] * (16 ** i)
        else:
            DEC += int(num_r[i]) * (16 ** i)

    BIN = []
    while True:
        temp = DEC % 2
        BIN.append(temp)
        DEC //= 2
        if DEC == 0:
            break

    while True:
        if len(BIN) % 4 == 0:
            break
        else:
            BIN.append(0)

    print(f"#{tc}", end=' ')
    for i in BIN[::-1]:
        print(i, end='')
    print()
