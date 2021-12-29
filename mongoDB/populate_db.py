import sys, os
sys.path.insert(0,os.path.abspath("./"))

from controller.db_handler import mongoDB

'''
Run this script to quickly populate the database from lib.json file
The format of lib.json should be as follows

{
    "Name" : "columbus",
    "Title" : "Christopher Columbus Monument",
    "Description" : "A statue of Christopher Columbus was installed in Christopher Columbus Waterfront Park, in Boston's North End, in the U.S. state of Massachusetts. On June 11, 2020,[2] the statue was removed for an undisclosed period after it was decapitated by protestors on the evening of June 9, 2020.",
    "Latitude" : "42.3613",
    "Longitude" : "71.0512",
    "ImagePath" : "/mongoDB/images/Columbus.jpg"
},
'''
db = mongoDB()
db.populate_db()

print("Complete!")


