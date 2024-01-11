alist=list()
for i in range(10):
    a=int(input())
    alist.append(a)
rlist=[]
for k in alist:
    remain = k%42
    rlist.append(remain)

rlist1=set(rlist)
rlist2=list(rlist1)

for j in range(10):
    rlist2.count(j)
# nonono
    


