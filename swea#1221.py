num_dic = {'ZRO':0,
           'ONE':1,
           'TWO':2,
           'THR':3,
           'FOR':4,
           'FIV':5,
           'SIX':6,
           'SVN':7,
           'EGT':8,
           'NIN':9}

r_num_dic = {y:x for x,y in num_dic.items() }

test = int(input())
for u in range(test):
    tc, case = input().split()
    lst = list(input().split())
    counts = [0 for _ in range(10)]

    for i in range(len(lst)):
        counts[num_dic[lst[i]]] += 1

    print(tc)
    for i in range(len(counts)):
        for k in range(counts[i]):
            print(r_num_dic[i],end = ' ')
    print()
