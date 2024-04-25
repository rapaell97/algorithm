def dfs(i):
    global arr
    temp.append(i)
    V[i] = 1
    next = lst[i]

    if V[next]:
        if next in temp:
            arr += temp[temp.index(next):]
        return
    else:
        dfs(next)


N = int(input())
lst = [0] + [int(input()) for _ in range(N)]
V = [0] * (N + 1)
arr = []

for i in range(1, N + 1):
    if not V[i]:
        temp = []
        dfs(i)

arr.sort()
print(len(arr))
for i in arr:
    print(i)
