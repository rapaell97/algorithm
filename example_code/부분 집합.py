def abc(n, path):
    global cnt

    if n == N:
        if sum(path) == 0:
            cnt += 1
            print(path)
        return
    abc(n + 1, path + [lst[n]])
    abc(n + 1, path)


lst = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(lst)
path = []
cnt = 0
abc(0, [])

print(cnt)
