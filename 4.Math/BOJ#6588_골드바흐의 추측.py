import sys
sys.stdin = open('a.txt', 'r')

M = 1000000
lst = [True] * (M + 1)
lst[0], lst[1] = False, False

for i in range(2, int(M ** 0.5) + 1):
    if lst[i]:
        for j in range(2 * i, M + 1, i):
            if lst[j]:
                lst[j] = False

while True:
    N = int(input())

    if N == 0:
        break

    check = False
    for i in range(2, M+1):
        if lst[i] and lst[N-i]:
            check = 1
            print(f"{N} = {i} + {N-i}")
            break

    if not check:
        print("Goldbach's conjecture is wrong.")


