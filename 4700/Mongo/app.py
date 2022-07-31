import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://kido4700:151111@cluster0.f2hcmfu.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["test"]

collection = db["test"]

post1 = {"_id": 0, "name": "tim"}
post2 = {"_id": 1, "name": "joe"}

results = collection.update_one({"_id":0}, {"$inc":{"hello":5}})

post_count = collection.count_documents({})
print(post_count)