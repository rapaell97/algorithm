import sys
sys.stdin = open('../a.txt', 'r')

def binary_search(n):
    global check

    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2

        if n == lst_1[mid]:
            check = 1
            return

        if n > lst_1[mid]:
            start = mid + 1

        elif n < lst_1[mid]:
            end = mid - 1


N = int(input())
lst_1 = list(map(int, input().split()))
M = int(input())
lst_2 = list(map(int, input().split()))

lst_1.sort()

for i in range(M):
    check = 0
    binary_search(lst_2[i])
    print(check, end=' ')