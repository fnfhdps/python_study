import tweepy
import json
from urllib import parse

consumer_key = 'L0QnhP203yP1lp9X02X0571R2'
consumer_secret = 'nqEVvw77IPdmwNB6QCt3QjGhQhgX2dZfw8layZZ2mcfKMKP9EJ'
access_token = '796556175147941888-WJqRJZCoi0YFthcaj1JluYCT85S1aQk'
access_secret = '1ObeYc4bEA4ZSq8Fy6SQRmH7Ubq3x6WQxtiVmNBcUD3OD'

#개인정보 인증 요청
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#액세스 요청
auth.set_access_token(access_token, access_secret)
#twitter API 생성
api = tweepy.API(auth)

keyword = '도지코인'

key = []
A = []

tweet = api.search(keyword, count = 500)

for tw in tweet:    # 트윗들 중에 하나씩 꺼내서tw에 저장  
    d = tw._json    # 트윗을 json으로 변환
    key.append(d)   # json들을 리스트에 저장
    
with open('text5.json', 'w', encoding='utf-8') as file1:
    # 리스트 안에 값들을 한번에 파일로 저장
    json.dump(key, file1, indent=2, sort_keys = True)

with open('text5.json', 'r', encoding='utf-8') as file2:
    # 파일안에 저장된 값 불러오기
    r = json.load(file2)
    
with open('jisu.text','w', encoding='utf-8') as file:
    for i in r:
        if 'RT' in i['text']: #RT는 제외하고 추출
            continue
        ID = 'ID : ' + i['user']['name'] #원하는 키워드 정보 추출
        TEXT = '|'+'  본문 : ' + i['text']
        user = ID + TEXT
        A.append(user)

    for line in A: #저장
        a = str(i)
        file.writelines(line)
        file.write('\n==================================================\n')
    

