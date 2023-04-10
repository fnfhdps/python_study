name = 'im JISU kim '
print(name.lower())
print(name.upper())
print(name[0].isupper())
print(len(name))
print(name.replace('JISU','JOTSU'))

index = name.index('i')
print(index)
index = name.index('i', index + 1) #두번째 i의 위치를 찾음
print(index)

print(name.find('i'))
# find는 찾는 값이 없으면 -1 반환 index는 오류

print(name.count('i'))

print('난 \'김지수다\' ')
print('난 \\김지수다\\ ')