test = int(input())
lst_size = 1001
lst = [[0] * lst_size for _ in range(lst_size)]

for i in range(test):
    sub_lst = list(map(int, input().split()))
    for m in range(sub_lst[0], sub_lst[0] + sub_lst[2]):
        for n in range(sub_lst[1], sub_lst[1] + sub_lst[3]):
            if lst[m][n] != i + 1:
                lst[m][n] = i + 1

cnt_lst = [0 for _ in range(test)]
for m in range(lst_size):
    for n in range(lst_size):
        if lst[m][n] != 0:
            cnt_lst[lst[m][n] - 1] += 1

print(cnt_lst)