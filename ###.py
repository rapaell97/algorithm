import sys
sys.stdin = open('a.txt', 'r')

for T in range(1, 11):
    N = int(input())
    lst = list(map(int, input().split()))

    i = 0
    while i < N:
        mx = max(lst)
        mn = min(lst)

        for j in range(100):
            if lst[j] == mx:
                lst[j] -= 1
                break

        for j in range(100):
            if lst[j] == mn:
                lst[j] += 1
                break

        i += 1

    print(f"#{T}", max(lst) - min(lst))