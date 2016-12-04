# python
import couchdb

server = couchdb.Server('http://127.0.0.1:5984/')
db = server['cloud_tweets_world']

sum  = 0
for i in db:
    if 'retweet_count' in db[i]:
        sum += db[i]['retweet_count']

print sum