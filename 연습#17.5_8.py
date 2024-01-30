map1 = [[3,55,42],[-5,-9,-10]]
pix = list()
for i in range(2):
    a=list(map(int,input().split()))
    pix.append(a)

for i in pix:
    for k in i:
        check = False
        for p in map1:
            for q in p:
                if k == q:
                    check = True
                    break
                else:
                    check = False
            if check is True:
                break
        if check is False:
            print("N",end=' ')
        else:
            print("Y",end=' ')
    print()