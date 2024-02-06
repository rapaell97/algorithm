h,w = map(int,input().split())
lst = [list(input()) for _ in range(h)]
for i in range(len(lst)):
    check = False
    for k in range(len(lst[i])):
        if not check and lst[i][k] == '.':
            lst[i][k] = -1
        elif lst[i][k] == 'c':
            check = True
            lst[i][k] = 0
            x = 1
        else:
            lst[i][k] = x
            x+=1

for i in lst:
    for k in i:
        print(k,end = ' ')
    print()
