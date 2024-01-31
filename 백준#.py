case = int(input())
lst = [input() for _ in range(case)]
lst_set = set(lst)
real_lst = list(lst_set)

real_lst.sort(key = lambda x:(len(x),x))

for i in real_lst:
    print(i)