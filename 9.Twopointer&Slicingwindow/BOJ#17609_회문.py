import sys
sys.stdin = open('../a.txt', 'r')

T = int(input())
for _ in range(T):
    word = input()
    if word == word[::-1]:
        print(0)

    else:
        S, E = 0, len(word)-1

        check = 2
        while S <= E:
            if word[S] == word[E]:
                S += 1
                E -= 1

            else:
                temp = word[S+1:E+1]
                if temp == temp[::-1]:
                    check = 1
                    break

                temp = word[S:E]
                if temp == temp[::-1]:
                    check = 1
                    break

                break

        print(check)

