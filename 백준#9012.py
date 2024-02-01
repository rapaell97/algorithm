test = int(input())
for _ in range(test):
    lst = list(input())
    left = list()
    check = 1
    for i in lst:
        if i == '(':
            left.append(i)
        else:
            if len(left) == 0:
                check = 0
                break
            else:
                left.pop()
    if len(left) != 0:
        check = 0

    if check == 0:
        print('NO')
    else:
        print('YES')
