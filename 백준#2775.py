tc = int(input())
for u in range(tc):
    floor = int(input())
    room = int(input())
    lst = [[0 for _ in range(room)]for _ in range(floor+1)]
    for i in range(room):
        lst[0][i] = i+1

    for i in range(1,floor+1):
        for k in range(room):
            lst[i][k] = sum(lst[i-1][0:k+1])

    print(lst[floor][room-1])