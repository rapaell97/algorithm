import sys
sys.stdin = open ('../my_input.txt', 'r')
def boy(x):
    for i in range(1, 101):
        temp = x * i

        if temp < N + 1:
            if lst[temp] == 0:
                lst[temp] = 1
            else:
                lst[temp] = 0
        else:
            break

def girl(x):

    if lst[x] == 0:
        lst[x] = 1
    else:
        lst[x] = 0

    i = 1
    while True:
        if 0 < x - i and x + i < N + 1:
            if lst[x + i] == lst[x - i]:

                if lst[x + i] == 0:
                    lst[x - i] = 1
                    lst[x + i] = 1

                else:
                    lst[x - i] = 0
                    lst[x + i] = 0
            else:
                break
        else:
            break

        i += 1

N = int(input())
lst = [0] + list(map(int, input().split()))

num = int(input())
for j in range(num):
    a, b = map(int, input().split())

    if a == 1:
        boy(b)
    else:
        girl(b)

for i in range(1, N+1):
    print(lst[i], end=" ")
    if i % 20 == 0 :
        print()
