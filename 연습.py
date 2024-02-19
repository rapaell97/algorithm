maps = ["X591X","X1X5X","X231X", "1XXX1"]
for i in range(len(maps)):
    for k in range(len(maps[i])):
        if maps[i][k].isdecimal() == True:
            print('yes')