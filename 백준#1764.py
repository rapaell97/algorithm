n,m = map(int,input().split())
n_lst = {input() for _ in range(n)}
m_lst = {input() for _ in range(m)}
ans_lst = list()
ans = list(n_lst.intersection(m_lst))
print(len(ans))
ans.sort()
for i in ans:
    print(i)