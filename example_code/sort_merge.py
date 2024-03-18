def merge_sort(A):
    if len(A) == 1:
        return A

    M = len(A) // 2

    left = A[:M]
    right = A[M:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(L, R):
    global ans

    result = [0] * (len(L) + len(R))
    l, r = 0, 0

    if L[-1] > R[-1]:
        ans += 1

    while l < len(L) and r < len(R):
        if L[l] < R[r]:
            result[l+r] = L[l]
            l += 1

        else:
            result[l+r] = R[r]
            r += 1

    while l < len(L):
        result[l+r] = L[l]
        l += 1

    while r < len(R):
        result[l+r] = R[r]
        r += 1

    return result

# import sys
# sys.stdin = open('a.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    ans = 0
    arr = merge_sort(lst)

    print(f"#{tc} {arr[N//2]} {ans}")

