import sys
# print('python', 'java', sep=',', end='?')
# print('뭣이 더 재밌을까요?')

# print('python', 'java', file=sys.stdout) #표준 출력
# print('python', 'java', file=sys.stderr) #표준 에러

#시험 성적
# scores = {'수학':0, '영어':50, '코딩':100}
# for subject, score in scores.items():
#     print(subject, score)
    
# #보기 좋게 줄 맞추기
# scores = {'수학':0, '영어':50, '코딩':100}
# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep=':') 
#     #subject: 8개의 공간을 확보 후 왼쪽으로 정렬
#     #score: 4개의 공간 확보 후 오른쪽 정렬

# #은행 대기 순번표 001, 002, 003...
# for num in range(1, 21):
#     print('대기번호: ' + str(num).zfill(3))
#     #zfill(3) 3 공간중 값이 없는 공간을 0으로 채움

answer = input('아무 값이나 입력하세요: ')
print('입력하신 값은 30' + answer + '입니다')