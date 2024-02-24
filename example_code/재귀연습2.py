def abc(level):
    print(level,end='')
    if level == 4:
        return
    abc(level+1)
    print(level,end='')
abc(0) #012343210

print()
def ab(level):
    if level == 3:
        return
    print(level,end='')
    ab(level+1)
    print(level,end='')
ab(0) #012210