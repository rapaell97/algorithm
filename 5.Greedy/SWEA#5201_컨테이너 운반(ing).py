import sys
sys.stdin = open ('../my_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):

    N, M = map(int, input().split())
    con = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    con_use = [0] * len(con)
    turck_use = [0] * len(truck)

