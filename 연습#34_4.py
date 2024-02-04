n = int(input())
lst = [list(input()) for _ in range(n)]
s = 0
e= n-1

while s<=e:
    m = (s+e)//2
    if lst[m][0] == '#':
        if lst[m+1][0] == '0':
            p = m
            break
        else:
            s = m+1
    else:
        e = m-1

s = 0
e = n-1
while s<=e:
    m = (s+e)//2
    if lst[p][m] == '#':
        if lst[p][m+1] == '0':
            q = m
            break
        else:
            s = m+1
    else:
        e = m-1
print(p,q)



