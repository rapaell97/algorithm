import sys

sys.stdin = open('../a.txt', 'r')

N = int(input())
M = int(input())
X = list(map(int, input().split()))

s = 0
e = N
ans = 0
while s <= e:
    mid = (s + e) // 2

    check = True
    light_s = 0
    for i in X:
        if i - mid <= light_s:
            light_s = i + mid
        else:
            check = False
            break

    if light_s < N:
        check = False

    if check:
        e = mid - 1
        ans = mid
    else:
        s = mid + 1

print(ans)
