import sys
sys.stdin = open('a.txt', 'r')

M = 10000000
lst = [True] * (M + 1)
lst[0], lst[1] = False, False

for i in range(2, int(M ** 0.5) + 1):
    if lst[i]:
        for j in range(2*i, M+1, i):
            if lst[j]:
                lst[j] = False

N = int(input())
for i in range(N, M+1):
    if lst[i]:
        temp = str(i)
        if temp == temp[::-1]:
            print(i)
            break
