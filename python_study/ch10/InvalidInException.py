class InvalidInException(Exception):
    def __init__(self, arg):
        super().__init__('정수가 아닙니다: {0}'.format(arg))
        
def convert_to_integer(text):
    if text.isdigit():
        return int(text)
    else:
        raise InvalidInException(text)

if __name__ == '__main__':
    try:
        print('숫자를 입력하세요: ')
        text = input()
        number = convert_to_integer(text)

    except InvalidInException as err:
        print('예외가 발생했습니다 ({0})'.format(err))

    else:
        print('정수 형식으로 변환되었습니다 : {0}({1}'\
              .format(number, type(number)))
