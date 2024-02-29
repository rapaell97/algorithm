import sys
input = sys.stdin.readline

N = int(input())
N_lst = list(map(int, input().split()))

M = int(input())
M_lst = list(map(int, input().split()))

dic = dict()

for i in range(N):
    if N_lst[i] in dic:
        dic[N_lst[i]] += 1
    else:
        dic[N_lst[i]] = 1

for i in range(M):
    print(dic.get(M_lst[i], 0), end=' ')
