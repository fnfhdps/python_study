n1 = int(input('2 이상의 정수를 입력하세요: '))
n2 = int(input('2 이상의 정수를 입력하세요: '))

def sosu(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        return True

hap = 0
for i in range(n1, n2+1):
    if(sosu(i)):
        hap += i
print(hap)

    