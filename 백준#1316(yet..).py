test = int(input())
word_list = list()
cnt=0

for i in range(test):
    word_list.append(input())

for k in word_list:
    len_word = len(k)
    group_word_check = True
    for m in range(len_word-1):
        for n in range(m+1,len_word):
            if k[m] != k[n]:
                continue
        else:
            for j in range(m+2,len_word):
                if k[m] != k[j]:
                    for l in range(j+1,len_word):
                        if k[m] != k[l]:
                            cnt+=1

print(cnt)
