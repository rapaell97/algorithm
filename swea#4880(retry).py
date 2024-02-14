def tourna(left, right):
    if left == right:
        return left
    else:
        left_win = tourna(left, (left+right)//2)
        right_win = tourna((left+right)//2 + 1, right)
        return win(left_win, right_win)

def win(a,b):
    if lst[a] == lst[b]:
        return a
    if lst[a] > lst[b]:
        if lst[a]-lst[b] == 1:
            return a
        else:
            return b
    if lst[a] < lst[b]:
        if lst[b]-lst[a] == 1:
            return b
        else:
            return a

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    print(f"#{tc} {tourna(0,N-1)+1}")
