chihoon=list()
for i in range(20):
    one = input().split()
    chihoon.append(one)
test={'A+':4.5,
      'A0':4.0,
      'B+':3.5,
      'B0':3.0,
      'C+':2.5,
      'C0':2.0,
      'D+':1.5,
      'D0':1.0,
      'F':0.0}


chihoon_sum=0.0
chihoon_testsum=0.0

for k in range(20):
    if chihoon[k][2] != 'P':
        chihoon_sum+=float(chihoon[k][1])
        chihoon_testsum+=float(chihoon[k][1])*(test[chihoon[k][2]])
    else:
        continue

print(chihoon_testsum/chihoon_sum)








