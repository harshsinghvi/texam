from os import path,getenv,urandom
import pymongo

MONGODB_URI = getenv("MONGO_DB_URI")


new_key=urandom(12)

db = pymongo.MongoClient(MONGODB_URI).texam
s= db.texam.find_one()
r  = db.texam.update_one({"_id":s["_id"]}, { "$set": { "auth": new_key } }).acknowledged

if r :
    f = open('key.py','w')
    f.write("AUTH = \"{}\"".format(new_key))
    f.close()
    print("OK")
else :
    print("not ok") 
