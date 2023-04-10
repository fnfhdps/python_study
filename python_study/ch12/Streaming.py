twitter_consumer_key = 'L0QnhP203yP1lp9X02X0571R2'
twitter_consumer_secret = 'nqEVvw77IPdmwNB6QCt3QjGhQhgX2dZfw8layZZ2mcfKMKP9EJ'
twitter_access_token = '796556175147941888-WJqRJZCoi0YFthcaj1JluYCT85S1aQk'
twitter_access_secret = '1ObeYc4bEA4ZSq8Fy6SQRmH7Ubq3x6WQxtiVmNBcUD3OD'

import json
import twitter
from collections import Counter

twitter_api = twitter.Api(consumer_key = twitter_consumer_key,
                          consumer_secret = twitter_consumer_secret,
                          access_token_key = twitter_access_token,
                          access_token_secret = twitter_access_secret)

query = ['코로나']
output_file_name = 'stream_result1.txt'

with open(output_file_name, 'w', encoding = 'utf-8') as output_file:
    
    stream = twitter_api.GetStreamFilter(track=query)

    while True:
        for tweets in stream:
            tweet = json.dumps(tweets, ensure_ascii=False)  
            print(tweet, file=output_file, flush=True)
                  
with open(output_file_name, 'r', encoding = 'utf-8') as file:

    lines = json.load(file)
    line = ''
    for line in lines:
        print(line, end='')
    
