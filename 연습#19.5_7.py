map_lst = [[3,5,1],[3,8,1],[1,1,5]]
bit =[list(map(int,input().split())) for _ in range(2)]
di = list()
dk = list()
for i in range(len(bit)):
    for k in range(len(bit[i])):
        di.append(i)
        dk.append(k)
max_sum = 0
max_i = 0
max_k = 0
for i in range(len(map_lst)):
    for k in range(len(map_lst[i])):
        temp = 0
        for j in range(3):
            ni = i + di[j]
            nk = k + dk[j]
            if 0<= ni <len(map_lst) and 0<= nk <len(map_lst[i]):
                temp += map_lst[ni][nk]
        if temp >= max_sum:
            max_sum = temp
            max_i = i
            max_k = k

print(f"({max_i},{max_k})")