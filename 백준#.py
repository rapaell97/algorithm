selo,galo = list(map(int,input().split()))
lst = list()

for i in range(selo):
    lst.append(list(input()))

min_cnt = galo*selo
ans_ga=0
ans_se=0

for k in range(galo-7):
    for i in range(selo-7):
        cnt_b = 0
        cnt_w = 0
        for m in range(k,k+8):
            for n in range(i,i+8):
                if lst[n][m] == "B":
                    cnt_b += 1
                else:
                    cnt_w += 1

        if abs(cnt_b-cnt_w)<min_cnt:
            min_cnt = abs(cnt_b-cnt_w)
            ans_se = i
            ans_ga = k
cnt = 0

lst=[[] for _ in range(8)]
for i in range(8):
        if i%2 == 0:
            lst[i] = ["W",BWBWBWB]


print(cnt)


















