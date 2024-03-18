import sys
sys.stdin = open('../a.txt', 'r')

N, M = map(int, input().split())
lst = []

for i in range(N):
    num = int(input())
    lst.append(num)

S = min(lst)
E = max(lst) * M
ans = E
while S <= E:
    mid = (S + E) // 2

    temp = 0
    for i in lst:
        temp += (mid//i)

    if temp >= M:
        ans = min(mid, ans)
        E = mid - 1

    else:
        S = mid + 1

print(ans)