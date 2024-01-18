h,m=list(map(int,input().split()))
plus_time=int(input())
addhour, addmin = divmod(plus_time,60)
rhour=h+addhour
rmin=m+addmin

if rmin<60:
    if rhour>=24:
        print(rhour-24,rmin)
    else:
        print(rhour,rmin)
else:
    if rhour+1>=24:
        print(rhour+1-24,rmin-60)
    else:
        print(rhour+1,rmin-60)



