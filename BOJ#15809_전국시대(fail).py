import sys

sys.stdin = open('a.txt', 'r')


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def union(x, y):
    x = find(x)
    if p[y] != y:
        union(x, find(y))

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
        P_team = p[P]
        Q_team = p[Q]
        team_P, team_Q = 0, 0

        for j in range(1, N + 1):
            if p[j] == P_team and lst[j] > team_P:
                team_P = lst[j]
            if p[j] == Q_team and lst[j] > team_Q:
                team_Q = lst[j]

        # print('전쟁')
        # print('P : ', P_team, team_P)
        # print('Q : ', Q_team, team_Q)

        if team_P > team_Q:
            lst[P_team] -= lst[Q_team]
            lst[Q_team] = 0
            union(P, Q)

        elif team_P < team_Q:
            lst[Q_team] -= lst[P_team]
            lst[P_team] = 0
            union(Q, P)

        else:
            lst[P_team] = 0
            lst[Q_team] = 0

    # print('########################')
    # print('i : ', i)
    # print('p : ', p)
    # print('list : ', lst)

for i in range(1, N + 1):
    find(i)

ans = 0
ans_lst = []
for i in lst:
    if i != 0:
        ans += 1
        ans_lst.append(i)

print(ans)
print(*ans_lst)
