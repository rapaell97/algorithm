def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if lst[x] > lst[y]:
        p[y] = x
        lst[x] += lst[y]
        lst[y] = 0

    else:
        p[x] = y
        lst[y] += lst[x]
        lst[x] = 0


N, M = map(int, input().split())
lst = [0]
for i in range(N):
    lst.append(int(input()))

p = [0] + list(range(1, N + 1))

for i in range(M):
    O, P, Q = map(int, input().split())

    if O == 1:
        union(P, Q)

    else:
        P = find(P)
        Q = find(Q)
        team_P, team_Q = lst[P], lst[Q]

        if team_P > team_Q:
            lst[P] -= lst[Q]
            lst[Q] = 0
            p[Q] = P

        elif team_P < team_Q:
            lst[Q] -= lst[P]
            lst[P] = 0
            p[P] = Q

        else:
            lst[P] = 0
            lst[Q] = 0

ans = 0
ans_lst = []
for i in lst:
    if i != 0:
        ans += 1
        ans_lst.append(i)

ans_lst.sort()
print(ans)
print(*ans_lst)
