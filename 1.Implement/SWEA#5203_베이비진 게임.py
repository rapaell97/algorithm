import sys
sys.stdin = open ('../my_input.txt', 'r')


def run1(arr):
    temp = list(set(arr))
    for i in range(len(temp)-2):
        if temp[i] + 1 == temp[i + 1] and temp[i + 1] + 1 == temp[i + 2]:
            return 1

    return 0


def triplet(arr):

    for i in range(len(arr)):
        temp = arr.count(arr[i])

        if temp >= 3:
            return 1

    return 0


N = int(input())
for tc in range(1, N+1):
    card = list(map(int, input().split()))

    player_1 = []
    player_2 = []

    i = 0
    win = False
    while i < len(card):

        if i % 2 == 0:
            player_1.append(card[i])

            if len(player_1) >= 3:
                player_1.sort()

                if run1(player_1) == 1:
                    print(f"#{tc} {1}")
                    win = True
                    break

                elif triplet(player_1) == 1:
                    print(f"#{tc} {1}")
                    win = True
                    break


        else:
            player_2.append(card[i])

            if len(player_2) >= 3:
                player_2.sort()

                if run1(player_2) == 1:
                    print(f"#{tc} {2}")
                    win = True
                    break

                if triplet(player_2) == 1:
                    print(f"#{tc} {2}")
                    win = True
                    break

        i += 1

    if not win:
        print(f"#{tc} {0}")

