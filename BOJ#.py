N = int(input())
lst = list(map(int, input().split()))
lst.sort()

S, E = 0, N-1
ans_i, ans_k = lst[S], lst[E]
ans = abs(lst[S] + lst[E])

while S < E:
    temp = lst[S] + lst[E]

    if abs(temp) < ans:
        ans = abs(temp)
        ans_i = lst[S]
        ans_k = lst[E]

    if temp < 0:
        S += 1
    else:
        E -= 1

print(ans_i, ans_k)

