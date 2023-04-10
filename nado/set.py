#집합 {}
#중복 안됨, 순서 없음

myset = {1,2,3,3,3}
print(myset)

java = {'유재석', '김태호', '양세형'}
python = set(['유재석', '박명수'])

#교집합 (java와 python을 모두 할 수 있는 사람)
print(java & python)
print(java.intersection(python))

#합집합 둘다 가능~
print(java | python)
print(java.union(python))

#차집합 (java는 할 줄 알지만 파이썬은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

#python할 줄 아는 사람이 늘어남
python.add('김태호')
print(python)

#java를 까먹음
java.remove('양세형')
print(java)
