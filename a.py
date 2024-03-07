import sys
sys.stdin = open('a.txt', 'r')


lst = [[1, 2], [3, 4]]
print(sum(map(sum, lst)))