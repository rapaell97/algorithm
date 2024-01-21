test = int(input())
test_list=list()

for i in range(test):
    tc=list(map(int,input().split()))
    test_list.append(tc)

test_list.sort(key = lambda x: (x[0], x[1]))

for j in test_list:
    print(*j)



