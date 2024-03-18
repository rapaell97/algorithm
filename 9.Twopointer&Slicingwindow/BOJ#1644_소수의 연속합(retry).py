N = int(input())

lst = [True] * (N+1)
lst[0], lst[1] = False, False
arr = []

for i in range(2, N+1):
    if lst[i]:
        arr.append(i)

        for j in range(2*i, N+1, i):
            if lst[j]:
                lst[j] = False

S, E = 0, 0
ans = 0

while E <= len(arr):
    temp = sum(arr[S:E])

    if temp > N:
        S += 1

    elif temp < N:
        E += 1

    else:
        ans += 1
        E += 1

print(ans)