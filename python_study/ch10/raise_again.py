def some_f():
    print('1-10사이의 수를 입력하세요: ')
    num = int(input())
    if num <1 or num > 10:
        raise Exception('유효하지 않은 숫자 입니다: {0}'.format(num))

    else:
        print('입력한 수는 {0}입니다'.format(num))

def some_f_caller():
    try:
        some_f()
    except Exception as err:
        print('1) 예외가 발생했습니다 {0}'.format(err))
        raise

try:
    some_f_caller()
except Exception as err:
    print('2) 예외가 발생했습니다 {0}'.format(err))
