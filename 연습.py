word = input()
print(len(word))
cnt=0
for i in word:
    if i == word[-1]:
        cnt+=1
print(cnt)