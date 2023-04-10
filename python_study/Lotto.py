from random import *
cho = []

for i in range(7):
    num = randint(1, 45)
    while num in cho:
        num = randint(1, 45)
    cho.append(num)

print('로또 추첨 번호')
print('로또 당첨 번호 {0}'.format(cho[:6]))
print('보너스 번호 [{0}]'.format(cho[6]))