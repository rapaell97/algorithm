num = int(input())
cnt_list = list()

for i in range(num//5+1):
    for k in range(num//3+1):
        if (5*i)+(3*k) == num:
            cnt_list.append(i+k)

if len(cnt_list) == 0:
    print(-1)
else:
    print(min(cnt_list))



