# score_file = open('score.txt', 'w', encoding='utf-8')
# print('수학 : 0', file=score_file)
# print('영어 : 50', file=score_file)
# score_file.close()

# score_file = open('score.txt', 'a', encoding='utf-8')
# score_file.write('과학 : 80')
# score_file.write('\n코딩 : 100')
# score_file.close()

# score_file = open('score.txt', 'r', encoding='utf-8')
# print(score_file.read())
# score_file.close()

# score_file = open('score.txt', 'r', encoding='utf-8')
# print(score_file.readline(), end='') #한 줄씩 읽기 커서는 다음 줄
# print(score_file.readline(), end='')
# print(score_file.readline(), end='')
# print(score_file.readline(), end='')

#가져온 파일은 몇 줄인지 모르니까 아는법
# score_file = open('score.txt', 'r', encoding='utf-8')
# while True:
#     line = score_file.readline() #한 줄씩 읽어옴
#     if not line: #읽을 줄이 없으면 멈춤
#         break
#     print(line, end='')
# score_file.close()

#리스트에 넣어서 출력
score_file = open('score.txt', 'r', encoding='utf-8')
lines = score_file.readlines() #리스트 형태로 저장
for line in lines:
    print(line, end='')
score_file.close() #파일 닫는게 정말 중요!