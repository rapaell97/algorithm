import sys
sys.stdin = open ('my_input.txt', 'r')

decoder = {
    "0001101": "0",
    "0011001": "1",
    "0010011": "2",
    "0111101": "3",
    "0100011": "4",
    "0110001": "5",
    "0101111": "6",
    "0111011": "7",
    "0110111": "8",
    "0001011": "9",
}

T = int(input())
for tc in range(1,T+1):
    N , M = map(int,input().split())
    lst = [list(map(int,input())) for _ in range(N)]

    check = False
    for i in range(N):
        for k in range(M):
            if lst[i][k] == 1:
                p_i = i
                check = True
                break
        if check:
            break

    for k in range(M-1, -1, -1):
        if lst[p_i][k] == 1:
            p_k = k
            break

    sample_lst = lst[p_i][p_k - 55: p_k + 1]
    sample_str = ''.join(map(str, sample_lst))

    temp = 0
    ans_lst = list()
    for i in range(0, len(sample_str), 7):
        ans_lst.append(int(decoder[sample_str[i:i+7]]))
        if (i+1) % 2 == 1:
            temp += (3 * int(decoder[sample_str[i:i+7]]))
        else:
            temp += int(decoder[sample_str[i:i+7]])

    if temp % 10 == 0:
        print(f"#{tc} ", sum(ans_lst))
    else:
        print(f"#{tc} ", 0)
