from pymongo import MongoClient
import pprint
from bson.objectid import ObjectId
client = MongoClient('localhost', 27017)

if __name__ == '__main__':
    db = client.mongo_db_lab
    definitions = db.definitions

    print("fetching all records\n")
    for definition in definitions.find():
        pprint.pprint(definition)

    print("\n\nfetching one record\n")
    pprint.pprint(definitions.find_one())
    
    print("\n\nfetching specific record (Capitaland)\n")
    pprint.pprint(definitions.find_one({"word": "Capitaland"}))

    print("\n\nfetching record by object id (Capitaland ... same as before)\n")
    pprint.pprint(definitions.find_one({"_id": ObjectId("56fe9e22bad6b23cde07b8cb")}) )

    print("\n\ninserting new record\n")
    definitions.insert_one({'word':'dino','definition':'A magical place where BBQ and alcohol meet in holy matrimony'}) 
    #proving word did show up
    pprint.pprint(definitions.find_one({"word": "dino"}))
                    
