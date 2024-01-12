alist=list()
for i in range(10):
    a=int(input())
    alist.append(a)
rlist=list()
for k in alist:
    remain = k%42
    rlist.append(remain)

rset=set(rlist)

print(len(rset))



    


