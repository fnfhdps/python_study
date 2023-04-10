my_list = [1,2,3,4,5]
def print_element(arg, index):
    try:
        print(arg[index])
    except Exception as err:
        print('제대로 치세요~ {0}'.format(err))

print_element()
