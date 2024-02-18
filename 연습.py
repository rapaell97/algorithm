T = int(input())
for tc in range(1,T+1):
    N , M = map(int,input().split())
    lst = [list(input()) for _ in range(N)]
    ans = 0
    for i in lst[0]:
        if i != 'W':
            ans += 1
    for i in lst[-1]:
        if i != 'R':
            ans += 1

    part_ans = (N-2)*M
    for i in range(1,N-1):
        temp = 0
        for k in range(len(lst[i])):
            if lst[i][k] != 'B':
                temp += 1

        for j in range(1,i):
            for k in range(len(lst[j])):
                if lst[j][k] != 'W':
                    temp += 1

        for j in range(i+1,N-1):
            for k in range(len(lst[j])):
                if lst[j][k] != 'R':
                    temp += 1
        if temp < part_ans:
            part_ans = temp

    print(f"#{tc} {ans+part_ans}")
