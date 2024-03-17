import sys
sys.stdin = open('../a.txt', 'r')

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
lst = list(map(list, zip(*lst)))
A = int(input())

ans = 0
for i in range(A):
    ans += sum(lst[i])

temp = ans
p = A
while p < M:
    temp += sum(lst[p])
    temp -= sum(lst[p-A])

    ans = max(ans, temp)
    p += 1

print(ans)






