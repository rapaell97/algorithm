lst = [['_', '_', '_', '_', '_'],
       ['_', '_', '_', '_', '_'],
       ['_', '_', '_', '_', '_'],
       ['_', '_', '_', '_', '_']]

def explode(arr,x,y):
    di = [-1,-1,0,1,1,1,0,-1]
    dk = [0,1,1,1,0,-1,-1,-1]

    for i in range(8):
        ni = x+di[i]
        nk = y+dk[i]

        if 0<= ni <4 and 0<= nk <5:
            arr[ni][nk] = '#'

for i in range(2):
    a,b = map(int,input().split())
    explode(lst,a,b)

for i in lst:
    for k in i:
        print(k,end=' ')
    print()