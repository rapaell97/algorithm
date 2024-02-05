test = int(input())
def check(word):
    start = 0
    for i in range(len(word)):
        cnt = 0
        alpha_cnt = word.count(word[start])
        for k in range(start,len(word)):
            if word[start] == word[k]:
                cnt+=1
            else:
                start=k
                break
        if alpha_cnt != cnt:
            return 0
    return 1

ans=0

for i in range(test):
    input_word=input()
    ret = check(input_word)
    ans+=ret
print(ans)
