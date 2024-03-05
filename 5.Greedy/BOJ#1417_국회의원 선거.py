N = int(input())
lst = [int(input()) for _ in range(N)]

cnt = 0
while True:
    if max(lst) == lst[0]:
        if lst.count(max(lst)) == 1:
            print(cnt)
            break
        else:
            print(cnt + 1)
            break

    m_idx = lst.index(max(lst))
    if m_idx != 0:
        lst[m_idx] -= 1
        lst[0] += 1
        cnt += 1