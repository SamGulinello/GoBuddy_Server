from pymongo import MongoClient, InsertOne
import pprint
import json

# Initiate MongoDB
client = MongoClient()
db = client.tourist
collection = db.landmarks

with open(r"database/lib.json") as f:
    myDict = json.loads(f.read())

result = collection.insert_one(myDict)

for doc in collection.find():
    pprint.pprint(doc)

client.close()
