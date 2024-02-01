lst=[[0 for _ in range(4)] for _ in range(4)]
x = 1
for i in range(len(lst)):
    for k in range(len(lst[i])):
        lst[i][k] = x
        x+=1

lst2 = [[0 for _ in range(4)] for _ in range(4)]
num = list(map(int,input().split()))

for j in range(len(num)):
    for i in range(len(lst)):
        for k in range(len(lst[i])):
            if num[j] == lst[i][k]:
                lst2[i][k] = j+1

for i in lst2:
    for k in i:
        print(k,end=' ')
    print()


