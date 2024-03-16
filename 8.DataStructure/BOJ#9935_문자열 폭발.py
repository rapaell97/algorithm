arr = list(input())
bomb = list(input())
ans = []
B = len(bomb)

for i in range(len(arr)):
    ans.append(arr[i])

    A = len(ans)
    if A >= B:
        if ans[A-B:A-B+B] == bomb:
            check = False
            for _ in range(B):
                ans.pop()

if len(ans) == 0:
    print('FRULA')

else:
    print(''.join(ans))
