import sys
sys.stdin = open('../a.txt', 'r')

N, D, K, C = map(int, input().split())
table = []

for _ in range(N):
    table.append(int(input()))

p1, p2 = 0, K-1
ans = 0
while p1 < N:
    temp = []
    if p2 >= N:
        p2 -= N

    if p1 > p2:
        temp = table[p1:] + table[:p2+1]
    else:
        temp = table[p1:p2+1]

    result = set([C] + temp)
    ans = max(ans, len(result))

    p1 += 1
    p2 += 1

print(ans)


