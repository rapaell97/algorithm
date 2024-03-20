import sys
sys.stdin = open('../a.txt', 'r')

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

d = [[0]*3 for _ in range(N)]
d[0] = lst[0]

for i in range(1, N):
    d[i][0] = min(d[i-1][1], d[i-1][2]) + lst[i][0]
    d[i][1] = min(d[i-1][0], d[i-1][2]) + lst[i][1]
    d[i][2] = min(d[i-1][0], d[i-1][1]) + lst[i][2]

print(min(d[N-1]))


