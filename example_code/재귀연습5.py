def abc(level):
    global cnt
    if level == 3:
        cnt += 1
        if temp == word:
            print(cnt)
        return
    for i in range(4):
        temp[level] = lst[i]
        abc(level+1)

lst = ['A','B','C','D']
word = list(input())
temp = ['']*3
cnt = 0
abc(0)