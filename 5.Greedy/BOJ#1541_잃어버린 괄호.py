arr = []
lst = list(input())

i, j = 0, 0
while j < len(lst):
    if lst[j] != '+' and lst[j] != '-':
        j += 1

    else:
        arr.append(''.join(lst[i:j]))
        arr.append(lst[j])
        i = j + 1
        j += 1

arr.append(''.join(lst[i:j]))
i = 0
ans = 0
check = True
while i < len(arr):
    if arr[i] == '-':
        temp = 0
        for k in range(i+1, len(arr), 2):
            if k == len(arr) - 1:
                temp += int(arr[k])
                i = k
                check = False

            else:
                if arr[k+1] == '+':
                    temp += int(arr[k])

                elif arr[k+1] == '-':
                    temp += int(arr[k])
                    i = k+1
                    break

        ans -= temp
    else:
        if i % 2 == 0:
            ans += int(arr[i])
        i += 1

    if not check:
        break
print(ans)











