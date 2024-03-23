N, M = map(int, input().split())
dic = {}

for _ in range(N):
    word = input()
    if len(word) < M:
        continue
    if dic.get(word):
        dic[word] += 1
    else:
        dic[word] = 1

ans = sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for i in ans:
    print(i[0])
