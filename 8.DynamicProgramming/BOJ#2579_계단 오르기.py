import sys
sys.stdin = open('../a.txt', 'r')

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

if N <= 2:
    print(sum(lst))
else:
    lst = [0] + lst

    d = [0] * (N + 1)

    d[1] = lst[1]
    d[2] = lst[1] + lst[2]
    for i in range(3, N + 1):
        d[i] = max(d[i - 2] + lst[i], d[i - 3] + lst[i - 1] + lst[i])

    print(d[-1])
