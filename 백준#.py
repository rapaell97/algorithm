def make_num(n,temp):
    global mx
    if n == M:
        if int(temp) < N:
            mx = max(int(temp),mx)
        return
    for i in range(len(lst)):
        make_num(n + 1, temp + lst[i])

N , K = map(int,input().split())
M = len(str(N))
lst = list(input().split())
mx = 0
make_num(0,'')
print(mx)
