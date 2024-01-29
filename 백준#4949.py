word_lst = list()
while True:
    word = input()
    if word == '.':
        break
    else:
        word_lst.append(list(word))


for j in range(len(word_lst)):
    left=list()
    cnt = 0
    for i in range(len(word_lst[j])):
        if word_lst[j][i] == '(' or word_lst[j][i] == '[':
            left.append(word_lst[j][i])
        elif word_lst[j][i] == ')':
            if len(left) == 0:
                cnt+=1
                break
            else:
                if left[-1] == '(':
                    left.pop()
                    word_lst[j][i]=-1
        elif word_lst[j][i] == ']':
            if len(left) == 0:
                cnt+=1
                break
            else:
                if left[-1] == '[':
                    left.pop()
                    word_lst[j][i] = -1

    for i in word_lst[j]:
        if i == ')' or i == ']':
            cnt+=1

    if len(left) == 0 and cnt == 0:
        print('yes')
    else:
        print('no')
