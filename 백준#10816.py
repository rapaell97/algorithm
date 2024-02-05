import sys
input = sys.stdin.readline
num1 = int(input())
all_cards = list(map(int,input().split()))
num2 = int(input())
check_cards = list(map(int,input().split()))
dic = dict()

for i in range(len(all_cards)):
    if all_cards[i] in dic:
        dic[all_cards[i]] += 1
    else:
        dic[all_cards[i]] = 1

for i in range(len(check_cards)):
    print(dic.get(check_cards[i],0),end=' ')
