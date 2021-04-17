import pymongo
from os import getenv

MONGODB_URI = getenv("MONGO_DB_URI")

db = pymongo.MongoClient(MONGODB_URI).texam
f = db.responses.find()
for i in f: 
    temp = {}
    flag = False
    for n, j in enumerate(i['responses']): 
        if j != None:
            temp[str(n)] = j
        else: 
            flag = True
    print(i)
    if flag:
        db.responses.update_one(i, {"$set":{'responses':temp}})


