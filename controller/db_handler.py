import pymongo
from pymongo.errors import ConnectionFailure
import pprint
import json

class mongoDB:
    def connect_db(self):
        client = pymongo.MongoClient("mongodb+srv://SamGulinello:Nessa@cluster0.8iwwt.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        db = client.test
        return client

    def get_dbCollection(self):

        # Initiate MongoDB
        db = self.client.test
        db = self.client.tourist
        collection = db.landmarks

        return collection

    def __init__(self):
        self.client = self.connect_db()
        self.collection = self.get_dbCollection()

    def close_db(self):
        #close MongoDB connectison
        self.client.close()

    def get_id(self, name):
        data = self.collection.find({"Name": name.upper()})
        return data[0]['_id']

    def get_title(self, id):
        data = self.collection.find({"_id": id})
        return data[0]['Title']

    def get_description(self, id):
        data = self.collection.find({"_id": id})
        return data[0]['Description']

    def get_imgPath(self, id):
        data = self.collection.find({"_id": id})
        return data[0]['ImagePath']
        
    def populate_db(self):
        # Initiate MongoDB
        self.collection = self.get_dbCollection()

        # Open JSON
        with open(r"mongoDB/lib.json") as f:
            myDict = json.loads(f.read())
            # Format Naming Convention
            for object in myDict:
                object["Name"] = object["Name"].upper()

        # Add Unique Items to MongoDB
        for landmark in myDict:
            if(self.collection.find_one({"Name":landmark["Name"]})): 
                pass
            else:
                result = self.collection.insert_one(landmark)
                print("Successfully Added " + landmark["Name"])

        # Print Database Objects
        for doc in self.collection.find():
            pprint.pprint(doc)
        
        self.close_db()
