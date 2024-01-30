# import sys
# sys.stdin = open("input1.txt", "r")

for u in range(10):
    case = int(input())
    lst = list()
    for i in range(100):
        a = list(map(int, input().split()))
        lst.append(a)

    sum_lst = list()

    for i in range(len(lst)):
        sum = 0
        for k in range(len(lst[i])):
            sum += lst[i][k]
        sum_lst.append(sum)

    for k in range(len(lst)):
        sum = 0
        for i in range(len(lst[i])):
            sum += lst[i][k]
        sum_lst.append(sum)

    for i in range(len(lst)):
        sum = 0
        for k in range(len(lst[i])):
            if i == k:
                sum += lst[i][k]
        sum_lst.append(sum)

    for i in range(len(lst)):
        sum = 0
        for k in range(len(lst[i])):
            if i+k == 99:
                sum += lst[i][k]
        sum_lst.append(sum)

    print(f"#{u+1} {max(sum_lst)}")



