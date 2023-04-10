import tweepy
import datetime

#트위터 개인 앱 계정에서 아래 4가지 사항 확인
consumer_key = 'L0QnhP203yP1lp9X02X0571R2'
consumer_secret = 'nqEVvw77IPdmwNB6QCt3QjGhQhgX2dZfw8layZZ2mcfKMKP9EJ'
access_token = '796556175147941888-WJqRJZCoi0YFthcaj1JluYCT85S1aQk'
access_token_secret = '1ObeYc4bEA4ZSq8Fy6SQRmH7Ubq3x6WQxtiVmNBcUD3OD'
#계정 승인
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#트윗 포스트하기
tweet = str(datetime.datetime.now()) + 'Brain Python Test'
api.update_status(status = tweet)

print('Succesfully Posted')
print()

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
