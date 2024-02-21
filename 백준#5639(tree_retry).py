def preorder(t):
    if t != '.':
        print(t, end='')
        preorder(tree[t][0])
        preorder(tree[t][1])

def inorder(t):
    if t != '.':
        inorder(tree[t][0])
        print(t, end='')
        inorder(tree[t][1])

def postorder(t):
    if t != '.':
        postorder(tree[t][0])
        postorder(tree[t][1])
        print(t, end='')

N = int(input())
tree = dict()
for i in range(N):
    temp = list(input().split())
    tree[temp[0]] = [temp[1], temp[2]]

preorder('A')
print()
inorder('A')
print()
postorder('A')
