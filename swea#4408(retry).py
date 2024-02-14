T = int(input())
for tc in range(1,T+1):
    N = int(input())
    use = [0 for _ in range(200+1)]
    lst = list()
    for i in range(N):
        a,b = map(int,input().split())
        lst.append([a,b])
    for i in range(len(lst)):
        lst[i].sort()

    for i in range(len(lst)):
        for j in range((lst[i][0]+1)//2,(lst[i][1]+1)//2+1):
            use[j] += 1

    time = max(use)
    print(f"#{tc} {time}")

