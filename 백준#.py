test = int(input())

for i in range(test):
    word_list = list(map(str,input().split()))

cnt=0

for k in word_list:
    len_word = len(k)
    for m in range(len_word-1):
        if k[m] != k[m+1]:
            for n in range(m+2,len_word):
                if k[n] == k[m]:
                    break
                else:
                    cnt+=1
        else:
            ## ??


print(cnt)
