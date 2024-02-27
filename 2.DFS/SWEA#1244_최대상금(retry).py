import sys
sys.stdin = open ('../my_input.txt', 'r')

def dfs(n):
    global ans

    if n == N:
        ans = max(ans, int(''.join(lst)))
        return

    for i in range(size - 1):
        for k in range(i + 1, size):
            lst[i], lst[k] = lst[k], lst[i]
            temp = int(''.join(lst))

            if (n, temp) not in use:
                dfs(n + 1)
                use.append((n, temp))

            lst[i], lst[k] = lst[k], lst[i]

T = int(input())
for tc in range(1, T + 1):
    a, b = input().split()
    lst = list(a)
    N = int(b)
    size = len(lst)
    use = []

    ans = 0
    dfs(0)
    print(f"#{tc} {ans}")
