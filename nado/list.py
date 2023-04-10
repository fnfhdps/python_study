subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ['유재석', '박명수', '조세호']

print(subway.index('조세호'))

subway.append('하하')
print(subway)

#중간에 넣기
subway.insert(1, '정형돈')
print(subway)

#뒤에서 부터 꺼냄, 스택
print(subway.pop())
print(subway.pop())
print(subway)

# 같은게 몇개 있는지
subway.append('유재석')
print(subway)
print(subway.count('유재석'))


#정렬 오름차순
num = [4,2,6,7,3]
num.sort()
print(num)

#뒤집기 내림차순
num.reverse()
print(num)

num.clear()
print(num)

#리스트 합치기
num = [4,2,6,7,3]
mix = [20, '조세호', True]
num.extend(mix)
print(num)