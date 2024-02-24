# 1 0123
def ABC(level):
    # print(level,end='')
    if level == 3:
        return
    ABC(level+1)
ABC(0)
# 2 012
def ABC(level):
    if level == 3:
        return
    # print(level)
    ABC(level+1)
ABC(0)
#3 210
def ABC(level):
    if level == 3:
        return
    ABC(level+1)
    #print(level,end='')
ABC(0)
# 4 0123210
def ABC(level):
    #print(level,end=' ')
    if level == 3:
        return
    ABC(level + 1)
    #print(level, end=' ')
ABC(0)
# 5 012210
def ABC(level):
    if level == 3:
        return
    #print(level,end='')
    ABC(level+1)
    #print(level,end='')
ABC(0)

