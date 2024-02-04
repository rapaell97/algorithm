def check(x,y):
    max_cnt = 0
    for i in range(len(x)):
        cnt = 0
        for k in range(len(y)):
            if x[i] == y[k]:
                cnt += 1
        if cnt>=max_cnt:
            max_cnt = cnt
    return max_cnt

test = int(input())
for u in range(test):
    a = input()
    b = input()
    print(f"#{u+1} {check(a,b)}")