a = int(input())
lsta = set(map(int,input().split()))
b = int(input())
lstb = list(map(int,input().split()))

for i in lstb:
    if i in lsta:
        print(1)
    else:
        print(0)