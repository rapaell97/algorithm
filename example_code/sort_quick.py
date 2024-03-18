def quick_sort(A, S, E):
    if S < E:
        M = partition(A, S, E)

        quick_sort(A, S, M-1)
        quick_sort(A, M+1, E)

def partition(A, S, E):
    P = A[S]
    i, j = S, E

    while i <= j:
        while i <= j and A[i] <= P:
            i += 1

        while i <= j and A[j] >= P:
            j -= 1

        if i < j:
            A[i], A[j] = A[j], A[i]

    A[S], A[j] = A[j], A[S]
    return j

import sys
sys.stdin = open('../a.txt', 'r')

T = int(input())
for tc in range(1 , T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    quick_sort(lst, 0, N-1)
    print(f"#{tc} {lst[N // 2]}")