def turn(arr,n):
    result = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]

    p = 0
    for k in range(n):
        q = 0
        for i in range(n-1,-1,-1):
            result[0][p][q] = arr[i][k]
            q += 1
        p += 1

    p = 0
    for i in range(n-1,-1,-1):
        q = 0
        for k in range(n-1,-1,-1):
            result[1][p][q] = arr[i][k]
            q += 1
        p += 1

    p = 0
    for k in range(n-1,-1,-1):
        q = 0
        for i in range(n):
            result[2][p][q] = arr[i][k]
            q += 1
        p += 1

    return result

test = int(input())
for u in range(test):
    nn = int(input())
    lst = [list(map(int,input().split())) for _ in range(nn)]
    r = turn(lst,nn)
    print(f"#{u+1}")
    for i in range(nn):
        for j in range(3):
            for k in range(nn):
                print(r[j][i][k], end="")
            print(" ", end="")
        print()



