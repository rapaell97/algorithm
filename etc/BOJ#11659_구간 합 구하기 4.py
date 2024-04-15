import sys
sys.stdin = open('../a.txt', 'r')

N, M = map(int, input().split())
lst = list(map(int, input().split()))
for n in range(N-1):
    lst[n+1] += lst[n]
lst = [0] + lst

for _ in range(M):
    i, j = map(int, input().split())
    print(lst[j] - lst[i-1])
