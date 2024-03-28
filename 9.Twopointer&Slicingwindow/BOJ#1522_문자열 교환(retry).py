import sys
sys.stdin = open('../a.txt', 'r')

lst = list(input())
size = lst.count('b')
arr = lst + lst

ans = len(lst)
for i in range(len(lst)):
    ans = min(ans, arr[i:i+size].count('a'))
print(ans)
