arr = list(map(int, input()))
n = 4
path = [0]*n
cnt=0

def abc(level):
    global cnt

    if level == n:
        cnt += 1
        return

    for i in range(5):
        if level > 0 and abs(path[level-1] - arr[i]) > 3 :
            continue
        path[level] = arr[i]
        abc(level+1)

abc(0)
print(cnt)