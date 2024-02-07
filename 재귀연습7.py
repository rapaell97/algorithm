# 중복 제거하며 한명제외하는 경우
lst = ['E','W','A','B','C']
used = [0 for _ in range(len(lst))]
out = input()
temp = ['']*4
def play(level):
    global used
    if level == 4:
        if used[lst.index(out)] == 0:
            for i in range(len(temp)):
                print(temp[i],end='')
            print()
        return
    for i in range(len(lst)):
        if used[i] == 1:
            continue
        temp[level] = lst[i]
        used[i] = 1
        play(level+1)
        used[i] = 0

play(0)