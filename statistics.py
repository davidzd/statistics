# python
import couchdb
import json

server = couchdb.Server('http://127.0.0.1:5984/')
db = server['cloud_tweets_world']

count = 0
sum = 0
dd = dict()
ld = dict()
models = []
user_list = []
gap = 50
f = open('statistics.txt', 'wb')

for i in db:
    # print loading
    if count == 10000:
        f.write(json.dumps(dict(models=models)) + '\n')
    if count % 10000 == 0:
        print sum
        f.write(json.dumps(dd) + '\n')
        f.write(str(sum) + '\n')
        f.write("*" * 10 + "fenggexian" + "*" * 10 + '\n')

    # device distribution
    if 'device' in db[i]:
        if db[i]['device'] in dd:
            dd[db[i]['device']] += 1
        else:
            dd[db[i]['device']] = 1

    # text length distribution
    if 'orig_text' in db[i]:
        length = len(db[i]['orig_text'].split())
        if str(length) in ld:
            ld[str(length)] += 1
        else:
            ld[str(length)] = 1

    if count < 10000:
        if 'device' in db[i] and 'retweet_count' in db[i] and 'text' in db[i] and 'created_at' in db[i] and 'sentiment' in db[i]:
            model = dict()
            model['device'] = db[i]['device']
            model['retweet_count'] = db[i]['retweet_count']
            model['length'] = len(db[i]['text'].split())
            model['hour'] = db[i]['created_at'].split(' ')[3].split(':')[0]
            model['sentiment'] = db[i]['sentiment']
            models.append(model)
    # # sentiment distribution.
    # if 'sentiment' in db[i] and type(db[i]['sentiment']) == int:
    #     sum += db[i]['sentiment']

    # # time distribution
    # if 'created_at' in db[i]:
    #     day = db[i]['created_at'].split(' ')[0]
    #     hour = str(db[i]['created_at'].split(' ')[3].split(':')[0])
    #     if day in ['Sat', 'Sun']:
    #         sig = 'weekend'
    #     else:
    #         sig = 'weekday'
    #
    #     if hour in td[sig]:
    #         td[sig][hour] += 1
    #     else:
    #         td[sig][hour] = 0
    #
    # # follower count
    # if 'user_followers_count' in db[i] and 'user_friends_count' in db[i] and 'user_id' in db[i]:
    #     if db[i]['user_id'] not in user_list:
    #         user_list.append(db[i]['user_id'])
    #         if str((db[i]['user_followers_count']) / gap) in fc['follower']:
    #             fc['follower'][str((db[i]['user_followers_count']) / gap)] += 1
    #         else:
    #             fc['follower'][str((db[i]['user_followers_count']) / gap)] = 1
    #
    #         if str((db[i]['user_friends_count']) / gap) in fc['friend']:
    #             fc['friend'][str((db[i]['user_friends_count']) / gap)] += 1
    #         else:
    #             fc['friend'][str((db[i]['user_friends_count']) / gap)] = 1
    count += 1

f.close()
print sum
