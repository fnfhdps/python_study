url = 'http://naver.com'
url = 'http://youtube.com'
str1 = url.replace('http://', '')
str1 = str1[:str1.index('.')]

password = str1[:3] + str(len(str1)) + str(str1.count('e')) + '!'
print('{0}의 비밀번호는 {1}입니다'.format(url, password))



