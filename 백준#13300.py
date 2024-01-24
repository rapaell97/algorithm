info = [[0 for _ in range(6)]for _ in range(2)]
student,room = list(map(int,input().split()))
for i in range(student):
    a, b = list(map(int, input().split()))
    info[a][b-1]+=1

cnt=0
for i in info:
    for k in i:
        if k != 0:
            if k<=room:
                cnt+=1
            else:
                if k%room == 0:
                    cnt+=k//room
                else:
                    cnt+=((k//room)+1)
print(cnt)
