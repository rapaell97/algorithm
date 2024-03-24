import sys
input = sys.stdin.readline

N = int(input())
pre_mx = [0] * 3
pre_mn = [0] * 3
mx = [0] * 3
mn = [0] * 3

for _ in range(N):
    lst = list(map(int, input().split()))
    mx[0] = max(pre_mx[0], pre_mx[1]) + lst[0]
    mx[1] = max(pre_mx[0], pre_mx[1], pre_mx[2]) + lst[1]
    mx[2] = max(pre_mx[1], pre_mx[2]) + lst[2]
    pre_mx[0], pre_mx[1], pre_mx[2] = mx[0], mx[1], mx[2]

    mn[0] = min(pre_mn[0], pre_mn[1]) + lst[0]
    mn[1] = min(pre_mn[0], pre_mn[1], pre_mn[2]) + lst[1]
    mn[2] = min(pre_mn[1], pre_mn[2]) + lst[2]
    pre_mn[0], pre_mn[1], pre_mn[2] = mn[0], mn[1], mn[2]

print(max(mx), min(mn))
