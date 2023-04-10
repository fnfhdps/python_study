twitter_consumer_key = 'L0QnhP203yP1lp9X02X0571R2'
twitter_consumer_secret = 'nqEVvw77IPdmwNB6QCt3QjGhQhgX2dZfw8layZZ2mcfKMKP9EJ'
twitter_access_token = '796556175147941888-WJqRJZCoi0YFthcaj1JluYCT85S1aQk'
twitter_access_secret = '1ObeYc4bEA4ZSq8Fy6SQRmH7Ubq3x6WQxtiVmNBcUD3OD'

import twitter
from collections import Counter

a = []

twitter_api = twitter.Api(consumer_key = twitter_consumer_key,
                          consumer_secret = twitter_consumer_secret,
                          access_token_key = twitter_access_token,
                          access_token_secret = twitter_access_secret)

query = '코로나'
statuses = twitter_api.GetSearch(term = query, count = 100)

#account = '@TheBlueHouseKR'
#statuses = twitter_api.GetUserTimeline(screen_name=account, count=200, include_rts=True, exclude_replies=False)


for status in statuses:
    for tag in status.hashtags:
        try:
            #print(tag.text) #????? 뭐지?
            #print('----------------------------------------------------------')
            a.append(tag.text)
           # if tag not in a
        except Exception as e:
           print(e)
           
n = Counter(a).most_common(20)
print(n)
