import json
import redis

# Create redis object route
redisS = redis.Redis(host='127.0.0.1',port=6379, db=0)
# Load json file
# jsonOpen = open('/Users/d.l.harris77953/Desktop/NSU/SPRING2023/CSC-488/GIT Repo/MeteoriteLanding_0212.json')
# try:
#     jFile = json.load(jsonOpen)
# finally:
#     jsonOpen.close()

jFile = open("/Users/d.l.harris77953/Desktop/NSU/SPRING2023/CSC-488/GIT Repo/MeteoriteLanding_0212.json", 'r')
json_data = json.load(jFile)
#Load meteorite data into database
redisS.set('MeteorLanding',json.dumps(json_data))
#Retrieve data from database
returnJson = json.loads(redisS.get('MeteorLanding').decode('utf-8'))

print(returnJson)

# redisS.echo("hellooooo world")