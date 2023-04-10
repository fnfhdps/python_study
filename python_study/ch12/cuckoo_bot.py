import tweepy
import datetime
import threading

def check_time(curr_hour):
    dt = datetime.datetime.now()

    if curr_hour != dt.hour:
        print(dt)
        curr_hour = dt.hour

        consumer_key = 'L0QnhP203yP1lp9X02X0571R2'
        consumer_secret = 'nqEVvw77IPdmwNB6QCt3QjGhQhgX2dZfw8layZZ2mcfKMKP9EJ'
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        access_token = '796556175147941888-WJqRJZCoi0YFthcaj1JluYCT85S1aQk'
        access_token_secret = '1ObeYc4bEA4ZSq8Fy6SQRmH7Ubq3x6WQxtiVmNBcUD3OD'
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)

        hour = 0
        
        if curr_hour == 0:
            hour = 24
        else:
            hour = curr_hour
        
        tweet = '@seanlab'
        for i in range(0, hour):
            tweet += '흠냐리'

        api.update_status(status=tweet)
        print('Successfully Posted')

    threading.Timer(1, check_time, args=[curr_hour]).start()

if __name__ == '__main__':
    check_time(-1)
