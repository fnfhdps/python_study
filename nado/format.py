# 방법1
#print('나는 %d살 입니다'%20)
#print('나는 %s를 사랑해'%'나')
#print('apple은 %c로 시작해요'%'a')
# %s로 정수, 문자 하나 다 가능
#print('나는 %s살 입니다'%20)
#print('나는 %s와 %s를 사랑해'%('말콤이', '나'))

# 방법2
#print('나는 {}살입니다.'.format(20))
# 제발 %d던 format이던 괄호 안에 넣자!!
#print('나는 {}와 {}를 사랑해'.format('말콤이', '나'))
# 괄호 비어있으면 그냥 순서대로 출력
# print('나는 {1}와 {0}를 사랑해'.format('말콤이', '나')
# 숫자나 명칭 넣으면 대맘대로 순서 출력

# 방법3
#print('나는 {age}살이며, {color}색을 좋아해요'.format(age=21, color='노란'))
#print('나는 {age}살이며, {color}색을 좋아해요'.format(color='노란', age=21))
