my_list = [1,2,3]

try:
    print('첨자를 입력하세요:')
    i = int(input())
    print('my_list[{0}]: {1}'.format(i, my_list[i]))

except Exception as err:
    print('예외가 발생했습니다 ({0})'.format(err))

else:
    print('리스트의 요소 출력에 성공했습니다')
