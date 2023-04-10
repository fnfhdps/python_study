from random import *

id = range(1,21)
id = list(id)

#ID = []
#for i in range(1, 21):
#    ID.append(i)

shuffle(id)

chicken = sample(id, 1)
num= id.index(chicken[0])
id.pop(num)

coffee =  sample(id, 3)

print('--당첨자 발표--')
print('치킨 당첨자: {0}'.format(chicken[0]))
print('커피 당첨자: {0}'.format(coffee[:]))
print('--축하합니다--')