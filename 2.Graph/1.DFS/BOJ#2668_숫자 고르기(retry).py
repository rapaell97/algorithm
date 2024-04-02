def dfs(i, t):
    V[i] = 1

    if V[lst[i]] == 0:
        dfs(lst[i], t)
    elif V[lst[i]] == 1 and lst[i] == t:
        arr.append(lst[i])


N = int(input())
lst = [0] + [int(input()) for _ in range(N)]

arr = []
for i in range(1, N + 1):
    V = [0] * (N + 1)
    dfs(i, i)

arr.sort()
print(len(arr))
for i in arr:
    print(i)
