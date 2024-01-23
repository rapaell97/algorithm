lst = [[0 for _ in range(100)] for _ in range(100)]
case = int(input())
paper = list()
for i in range(case):
    a = list(map(int,input().split()))
    paper.append(a)

for k in range(len(paper)):
    for m in range(paper[k][0],paper[k][0]+10):
        for n in range(paper[k][1],paper[k][1]+10):
            if lst[m][n] == 0:
                lst[m][n] = 1
cnt = 0
for l in lst:
    for t in l:
        if t == 1:
            cnt+=1

print(cnt)




