num = int(input())
find = int(input())
lst = [[0 for _ in range(num)]for _ in range(num)]
di = [1,0,-1,0]
dk = [0,1,-0,-1]
i,k,d = 0,0,0
for j in range(num**2,0,-1):
    lst[i][k] = j
    ni = i+di[d]
    nk = k+dk[d]
    if 0<= ni <num and 0<= nk <num and lst[ni][nk] == 0:
        i = ni
        k = nk
    else:
        d = (d+1)%4
        i = i+di[d]
        k = k+dk[d]
for i in lst:
    for k in i:
        print(k,end=' ')
    print()

for i in range(len(lst)):
    for k in range(len(lst[i])):
        if lst[i][k] == find:
            print(i+1,k+1)
            break

