lst = [True for _ in range(1000000+1)]
for i in range(2,int(1000000**0.5)+1):
    if lst[i] == True:
        for k in range(2*i,1000001,i):
            lst[k] = False
lst[0],lst[1] = False,False
tc = int(input())
for u in range(tc):
    cnt = 0
    num = int(input())
    i = 0
    while i <= num//2:
        if lst[i] is True and lst[num-i] is True:
            cnt += 1
        i += 1
    print(cnt)


