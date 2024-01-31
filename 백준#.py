case = int(input())
lst = list(map(int,input().split()))
max_score = max(lst)
new_lst = list()

for i in lst:
    ns = i/max_score*100
    new_lst.append(ns)

print(sum(new_lst)/case)