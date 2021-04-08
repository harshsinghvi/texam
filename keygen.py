from os import path,getenv,urandom
import pymongo
from base64 import b64encode

newClient_key  = b64encode(urandom(12)).decode('utf-8')
newAdmin_key = b64encode(urandom(12)).decode('utf-8')

MONGODB_URI = getenv("MONGO_DB_URI")


db = pymongo.MongoClient(MONGODB_URI).texam
s = db.keys.find_one({"name":"Client Key"})
r  = db.keys.update_one({"_id":s["_id"]}, { "$set": { "auth": newClient_key } }).acknowledged

t = db.keys.find_one({"name":"Admin Key"})
u = db.keys.update_one({"_id":s["_id"]}, { "$set": { "auth": newAdmin_key } }).acknowledged

keys = str(
    {
        "Client_Key":newClient_key,
        "Admin_Key":newAdmin_key
    }
)

if r :
    f = open('key.txt','w')
    f.write(keys)
    f.close()
    print("OK")
else :
    print("not ok") 
