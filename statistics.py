# python
import couchdb

server = couchdb.Server('http://127.0.0.1:5984/')
db = server['cloud_tweets_world']

sum  = 0
count = 0
for i in db:
    if count%10000 == 0:
        print sum
    if 'retweet_count' in db[i]:
        sum += db[i]['retweet_count']
print sum