def dalpeng(x):
    lst = [[0 for _ in range(x)] for _ in range(x)]
    di = [0,1,0,-1]
    dk = [1,0,-1,0]
    num = x**2
    d = 0
    i,k = 0,0
    for j in range(1,num+1):
        lst[i][k] = j
        ni = i + di[d]
        nk = k + dk[d]

        if 0 <= ni < x and 0 <= nk < x and lst[ni][nk] == 0:
            i,k = ni,nk
        else:
            d = (d+1) % 4
            i = i + di[d]
            k = k + dk[d]
    return lst

test = int(input())
for u in range(test):
    case = int(input())
    print(f"#{u+1}")
    for i in dalpeng(case):
        for k in i:
            print(k,end=' ')
        print()
