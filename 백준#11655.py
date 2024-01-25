a= input()
lst = list()
for i in range(len(a)):
    lst.append(a[i])

for i in range(len(lst)):
    if lst[i] == ' ':
        continue
    if lst[i].isdigit() == False:
        if lst[i].islower() == True:
            if ord(lst[i])+13 <= 122:
                lst[i]=chr(ord(lst[i])+13)
            else:
                lst[i]=chr((ord(lst[i])+13)%122+96)
        else:
            if ord(lst[i]) + 13 <= 90:
                lst[i] = chr(ord(lst[i]) + 13)
            else:
                lst[i] = chr((ord(lst[i]) + 13)%90 + 64)
print(''.join(lst))




