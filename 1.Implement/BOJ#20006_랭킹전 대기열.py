import sys
input = sys.stdin.readline

dic = {}
lst = []
P, M = map(int, input().split())
R = 0
for i in range(P):
    l, n = input().split()

    if i == 0:
        dic[R] = [(int(l), n)]
        lst.append(int(l))
        R += 1
        continue

    check = False
    for j in range(len(lst)):
        if lst[j] - 10 <= int(l) <= lst[j] + 10 and len(dic[j]) < M:
            check = True
            dic[j].append((int(l), n))
            break

    if not check:
        dic[R] = [(int(l), n)]
        lst.append(int(l))
        R += 1

for i in range(len(dic)):
    dic[i].sort(key=lambda x: x[1])
    if len(dic[i]) == M:
        print('Started!')
        for j in range(len(dic[i])):
            print(*dic[i][j])

    else:
        print('Waiting!')
        for j in range(len(dic[i])):
            print(*dic[i][j])
