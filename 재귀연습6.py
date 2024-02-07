# 해당문자 진입하지 않는 경우
lst = list(input())
temp = ['']*4
cnt = 0
def abc(level):
    global cnt
    if level == 4:
        cnt += 1
        return

    for i in range(4):
        if level>0 and temp[level-1] == 'B' and lst[i] == 'T':
            continue
        if level>0 and temp[level-1] == 'T' and lst[i] == 'B':
            continue
        temp[level] = lst[i]
        abc(level+1)
abc(0)
print(cnt)

