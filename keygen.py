from os import path,getenv,urandom
import pymongo
from base64 import b64encode

new_key  = b64encode(urandom(12)).decode('utf-8')


MONGODB_URI = getenv("MONGO_DB_URI")


db = pymongo.MongoClient(MONGODB_URI).texam
s= db.texam.find_one()
r  = db.texam.update_one({"_id":s["_id"]}, { "$set": { "auth": new_key } }).acknowledged

if r :
    f = open('key.txt','w')
    f.write(new_key)
    f.close()
    print("OK")
else :
    print("not ok") 
