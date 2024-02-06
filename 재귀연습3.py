def abc(level):
    print('@', end='')
    if level == 2:
        print('*', end='')
        return
    
    for i in range(2):
        abc(level + 1)
        print('#', end='')
abc(0)