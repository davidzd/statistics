# python
import couchdb
import json

server = couchdb.Server('http://127.0.0.1:5984/')
db = server['cloud_tweets_world']

sum  = 0
count = 0
td = dict()
fc = dict(follower=dict(), friend=dict())
td['weekend'] = dict()
td['weekday'] = dict()
user_list = []
gap = 50
f = open('statistics.txt', 'wb')

for i in db:
    # print loading
    if count%10000 == 0:
        print sum
        f.write(json.dumps(td))
        f.write(json.dumps(td)+'\n')
        f.write(str(sum)+'\n')
        f.write(json.dumps(fc)+'\n')
        f.write("*"*10 + "fenggexian" + "*"*10+'\n')

    # sentiment distribution.
    if 'sentiment' in db[i] and type(db[i]['sentiment']) == int:
        sum += db[i]['sentiment']

    # time distribution
    if 'created_at' in db[i]:
        day = db[i]['created_at'].split(' ')[0]
        hour = str(db[i]['created_at'].split(' ')[3].split(':')[0])
        if day in ['Sat', 'Sun']:
            sig = 'weekend'
        else:
            sig = 'weekday'

        if hour in td[sig]:
            td[sig][hour] += 1
        else:
            td[sig][hour] = 0

    # follower count
    if 'user_followers_count' in db[i] and 'user_friends_count' in db[i] and 'user_id' in db[i]:
        if db[i]['user_id'] not in user_list:
            user_list.append(db[i]['user_id'])
            if str((db[i]['user_followers_count'])/gap) in fc['follower']:
                fc['follower'][str((db[i]['user_followers_count'])/gap)] += 1
            else:
                fc['follower'][str((db[i]['user_followers_count']) / gap)] = 1

            if str((db[i]['user_friends_count'])/gap) in fc['friend']:
                fc['friend'][str((db[i]['user_friends_count']) / gap)] += 1
            else:
                fc['friend'][str((db[i]['user_friends_count']) / gap)] = 1
    count += 1

f.close()
print td, sum, fc