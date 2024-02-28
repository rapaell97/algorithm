# 조합
# 주사위 눈금 N개를 던져서 나올 수 있는 모든 조합을 출력하시오 (N = 3 인 경우)
def dfs(n, start):
    if n == 3:
        print(ans)
        return

    for j in range(start, N):
        ans[n] = arr[j]
        dfs(n + 1, j)


arr = [1, 2, 3, 4, 5, 6]
N = len(arr)
ans = [0] * 3

dfs(0, 0)
