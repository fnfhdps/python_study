
for i in range(1,21):
    with open('{0}주차.txt'.format(i), 'w', encoding='utf-8') as report:
        report.write('-{0}주차 주간보고-'.format(i))
        report.write('\n부서 : ')
        report.write('\n이름 : ')
        report.write('\n업무 요약 : ')