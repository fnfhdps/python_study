import tweepy
import json

consumer_key = 'L0QnhP203yP1lp9X02X0571R2'
consumer_secret = 'nqEVvw77IPdmwNB6QCt3QjGhQhgX2dZfw8layZZ2mcfKMKP9EJ'
access_token = '796556175147941888-WJqRJZCoi0YFthcaj1JluYCT85S1aQk'
access_secret = '1ObeYc4bEA4ZSq8Fy6SQRmH7Ubq3x6WQxtiVmNBcUD3OD'

#개인 정보 인증 요청
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#엑세스 요청
auth.set_access_token(access_token, access_secret)
#twitter API 생성
api = tweepy.API(auth)

location = '%s,%s,%s'%("35.95", "128.25", "1000km") #검색기준 좌표, 반지름
keyword = '유튜브' #OR로 검색어 묶어줌, 검색어 5개, OR 대문자
key = []
add = []

#twitter 검색 cursor 선언
cursor = tweepy.Cursor(api.search,
                    q=keyword,
                    since = '2010-01-22', #이후 작성된 트윗
                    count = 50, #페이지당 반환할 트위터 수 최대 100
                    geocode = location, #검색 반경 조건
                    include_entities = True)


# for tw in cursor:
#     tw = tw._json
#     key.append(tw) #json으로 변환
    #리스트 안에 값들을 한번에 파일로 저장
    
with open('cursor.json', 'w', encoding='utf-8') as file:
    for i, tweet in enumerate(cursor.items()):
        tw = tweet._json
        #print('{0}:{1}'.format(i, tweet.items))
        json.dump(tw, file, indent=2, sort_keys = True)

with open('cursor.json', 'r', encoding='utf-8') as file:
    #파일에 저장된 값 일어오기
    r = json.load(file)

with open('cursor.text','w', encoding='utf-8') as file:
    for i in r:
        if 'RT' in i['text']: #RT는 제외하고 추출
            continue
        ID = 'ID : ' + i['user']['name'] #원하는 키워드 정보 추출
        TEXT = '|'+'  본문 : ' + i['text']
        user = ID + TEXT
        A.append(user)

    for line in A: #저장
        file.writelines(line)
        file.write('\n==================================================\n')
    
