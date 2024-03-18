N = int(input())
lst = list(map(int, input().split()))
lst.sort()

result = abs(lst[0] + lst[N-1])
ans_1, ans_2 = lst[0], lst[N-1]
S = 0
E = N - 1

while S < E:
    temp = lst[S] + lst[E]

    if abs(temp) < result:
        result = abs(temp)
        ans_1 = lst[S]
        ans_2 = lst[E]

        if result == 0:
            break

    if temp < 0:
        S += 1
    else:
        E -= 1

print(ans_1, ans_2)