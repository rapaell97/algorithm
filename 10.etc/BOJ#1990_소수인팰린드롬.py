import sys
input = sys.stdin.readline
sys.stdin = open('../a.txt', 'r')

A, B = map(int, input().split())
if B > 10**7:
    B = 10**7
lst = [True] * (B+1)
lst[0],lst[1] = False, False

for i in range(2, B+1):
    if lst[i]:
        for j in range(2*i, B+1, i):
            if lst[j]:
                lst[j] = False

for i in range(A, B+1):
    if lst[i]:
        temp = str(i)
        if temp == temp[::-1]:
            print(temp)

print(-1)