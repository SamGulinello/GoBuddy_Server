from pymongo import MongoClient, InsertOne
import pprint
import json

# Initiate MongoDB
client = MongoClient("mongodb+srv://SamGulinello:Nessa@testcluster.8iwwt.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test
db = client.tourist
collection = db.landmarks

# Open JSON
with open(r"database/lib.json") as f:
    myDict = json.loads(f.read())
    # Format Naming Convention
    for object in myDict:
        object["Name"] = object["Name"].upper()

# Add Unique Items to MongoDB
for landmark in myDict:
    if(collection.find_one({"Name":landmark["Name"]})):
        pass
    else:
        result = collection.insert_one(landmark)
        print("Successfully Added " + landmark["Name"])

# Print Database Objects
for doc in collection.find():
    pprint.pprint(doc)

# Close Database
client.close()
