lst = [[0 for _ in range(1002)] for _ in range(1002)]

test = int(input())
paper = list()
for i in range(test):
    sub_lst = list(map(int,input().split()))
    paper.append(sub_lst)
i=1
for k in range(len(paper)):
    for m in range(paper[k][0],paper[k][2]):
        for n in range(paper[k][1],paper[k][3]):
            if lst[m][n] != i:
                lst[m][n] = i
    i+=1

for b in range(test):
    print(lst.count(b+1))

