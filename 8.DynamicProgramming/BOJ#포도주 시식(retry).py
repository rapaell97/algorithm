N = int(input())
lst = [0] * 10001
d = [0] * 10001
for i in range(1, N + 1):
    lst[i] = int(input())

d[1] = lst[1]
d[2] = lst[1] + lst[2]
for i in range(3, N + 1):
    d[i] = max(d[i - 2] + lst[i], d[i - 3] + lst[i - 1] + lst[i], d[i - 1])

print(d[N])
