import sys

sys.stdin = open('../a.txt', 'r')

MN, MX = map(int, input().split())

lst = [0] * (MX - MN + 1)
ans = MX - MN + 1

for i in range(2, int(MX ** 0.5) + 1):
    square = i ** 2
    print((((MN - 1) // square) + 1) * square, MX+1)
    for j in range((((MN - 1) // square) + 1) * square, MX + 1, square):
        if not lst[j - MN]:
            lst[j - MN] = 1
            ans -= 1

print(ans)
