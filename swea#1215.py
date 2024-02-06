for u in range(1,11):
    num = int(input())
    lst = [list(input()) for _ in range(8)]

    cnt = 0
    for i in range(8):
        for k in range(8-(num-1)):
            temp = lst[i][k:k+num]
            if temp == temp[::-1]:
                cnt += 1

    for k in range(8):
        for i in range(8-(num-1)):
            temp = list()
            for j in range(num):
                temp.append(lst[i+j][k])
            if temp == temp[::-1]:
                cnt += 1

    print(f"#{u} {cnt}")