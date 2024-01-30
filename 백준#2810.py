num = int(input())
lst = list(input())

cnt = 1
i = 0
while i < len(lst):
    if lst[i] == 'S':
        cnt += 1
        i += 1

    else:
        i += 2
        cnt += 1

if cnt > num:
    print(num)
else:
    print(cnt)