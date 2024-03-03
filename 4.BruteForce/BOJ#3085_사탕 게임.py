import sys
sys.stdin = open('../a.txt', 'r')

def eat(arr):
    garo = 0
    for i in range(N):
        temp = 1
        for k in range(N - 1):
            if arr[i][k] == arr[i][k + 1]:
                temp += 1
                if temp > garo:
                    garo = temp
            else:
                temp = 1

    sero = 0
    for k in range(N):
        temp = 1
        for i in range(N - 1):
            if arr[i][k] == arr[i + 1][k]:
                temp += 1
                if temp > sero:
                    sero = temp
            else:
                temp = 1

    result = max(sero, garo)
    return result

N = int(input())
lst = [list(input()) for _ in range(N)]
di = [-1, 0, 1, 0]
dk = [0, 1, 0, -1]

ans = 0
for i in range(N):
    for k in range(N):
        for j in range(4):
            ni = i + di[j]
            nk = k + dk[j]

            if 0<= ni <N and 0<= nk <N and lst[i][k] != lst[ni][nk]:
                lst[i][k], lst[ni][nk] = lst[ni][nk], lst[i][k]
                ans = max(ans, eat(lst))
                lst[i][k], lst[ni][nk] = lst[ni][nk], lst[i][k]

print(ans)

