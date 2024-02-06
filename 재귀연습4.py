lst = ['a','b','c']
def abc(level):
    if level == 2:
        print(''.join(path))
        return

    for i in range(3):
        path[level]=lst[i]
        abc(level+1)
path=['']*2
abc(0)
