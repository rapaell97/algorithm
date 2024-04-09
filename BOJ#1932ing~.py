import sys
sys.stdin = open('a.txt', 'r')

N = int(input())
lst = []

for i in range(N):
    lst.append(list(map(int, input().split())))

d = [[] for _ in range(N)]
d[0] = lst[0]
d[1].append(d[0][0] + lst[1][0])
d[1].append(d[0][0] + lst[1][1])

for i in range(2, N):
    for j in range(i+1):
        temp = d[i-1][j]