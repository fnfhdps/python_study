#출석번호가 1,2,3,4,5 앞에 100을 붙이기로함 -> 101,102...
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

#학생 이름을 길이로 변환
students = ['아이언맨', '토르', '그루트']
students = [len(i) for i in students]
print(students)

#학생 이름을 대문자로 변환
students = ['iron man', 'thor', 'i am groot']
students = [i.upper() for i in students]
print(students)