line = list(input())
word = list(input())
cnt = 0

i=0
while i <=  len(line)-len(word):
    if line[i:i+len(word)] ==  word:
        cnt+=1
        i+=len(word)
    else:
        i+=1

print(cnt)




