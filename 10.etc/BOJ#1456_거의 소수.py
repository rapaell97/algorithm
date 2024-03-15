import sys
input = sys.stdin.readline

A, B = map(int, input().split())
lst = [True] * (int(B ** 0.5) + 1)
lst[0], lst[1] = False, False

for i in range(2, int(B ** 0.5) + 1):
    if lst[i]:
        for j in range(2*i, int(B ** 0.5)+1, i):
            if lst[j]:
                lst[j] = False

cnt = 0
for i in range(2, int(B ** 0.5)+1):
    if lst[i]:
        k = 2
        while i ** k <= B:
            if A <= i ** k:
                cnt += 1
            k += 1
print(cnt)