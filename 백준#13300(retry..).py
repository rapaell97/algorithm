student,room = list(map(int,input().split()))

lst = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
count = 0

for i in range(student):
    a, b = map(int,input().split())
    lst[a][b] += 1

for i in range(2):
    for j in range(1,7):
        if lst[i][j]%room == 0:
            count += lst[i][j]//room
        else:
            count += lst[i][j]//room+1

print(count)