test = int(input())
for u in range(test):
    num = int(input())
    scores = list(map(int,input().split()))
    cnt = [0]*101

    for i in scores:
        cnt[i]+=1
    m = max(cnt)

    m_lst = list()
    for k in range(len(cnt)):
        if cnt[k]==m:
            m_lst.append(k)

    print(f"#{u+1} {m_lst[-1]}")




