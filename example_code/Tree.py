'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

N = int(input())
lst = list(map(int,input().split()))

left = [0] * (N + 1)
right = [0] * (N + 1)

for i in range(N-1):
    p = lst[i * 2]
    c = lst[i * 2 + 1]

    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c

# 전위 순회
def pre_order(t):
    # t번 노드 존재하면
    if t:
        print(t,end=' ')
        pre_order(left[t])
        pre_order((right[t]))
print('########## 전위 순회 ##########')
pre_order(1)
print()

def inorder(t):
    if t:
        inorder(left[t])
        print(t,end=' ')
        inorder(right[t])

print('########## 중위 순회 ##########')
inorder(1)
print()

def postorder(t):
    if t:
        postorder(left[t])
        postorder(right[t])
        print(t, end = ' ')

print('########## 후위 순회 ##########')
postorder(1)
print()