word_list = list()
max_len=0

for i in range(5):
    word = input()
    one_list=list(word)
    if len(one_list)>max_len:
        max_len=len(one_list)
    word_list.append(one_list)

for k in range(len(word_list)):
    if len(word_list[k]) != max_len:
        add_list = max_len - len(word_list[k])
        for w in range(add_list):
            word_list[k].append(None)


for m in range(max_len):
    for n in range(len(word_list)):
        if word_list[n][m] != None:
            print(word_list[n][m],end='')


