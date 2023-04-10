cabinet = {3:'유재석', 100:'김태호'}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

#대괄호로 없는 값 가져오면 프로그램 종료
#print(cabinet[5])
#get으로 없는 값 가져오면 None 이라고 뜸
print(cabinet.get(5))
#5라는 값이 없으면 뒤에 문구 출력, 빈자리라고 알려주는듯
print(cabinet.get(5, '사용가능'))

print(3 in cabinet)
print(5 in cabinet)

#추가
cabinet = {'A-3':'유재석', 'B-100':'김태호'}
cabinet['A-3'] = '김종국' #덮어 쓰기
cabinet['C-20'] = '조세호' #추가 가능
print(cabinet)

#지우기
del cabinet['A-3']
print(cabinet)

#key만 출력
print(cabinet.keys())

#value만 출력
print(cabinet.values())

# 둘다 출력
print(cabinet.items())

#비우기
cabinet.clear()
print(cabinet)

