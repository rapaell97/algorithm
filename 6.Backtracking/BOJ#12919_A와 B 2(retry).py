def func(arr, cnt):
    global check

    if cnt == len(S):
        if arr == S:
            check = 1
        return

    if arr[-1] == 'A':
        func(arr[:-1], cnt - 1)
    if arr[0] == 'B':
        arr.reverse()
        func(arr[:-1], cnt - 1)


S = list(input())
T = list(input())

check = 0
func(T, len(T))

if check:
    print(1)
else:
    print(0)
