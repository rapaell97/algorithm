num = int(input())
r=1
for i in range(1,num+1):
    r*=i
cnt = 0
r=str(r)
for i in r[::-1]:
    if i == '0':
        cnt+=1
    else:
        print(cnt)
        break