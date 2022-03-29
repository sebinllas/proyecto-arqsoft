import pymongo
client = pymongo.MongoClient(
    "mongodb+srv://sebin:CcnHXTrCinlkVE9m@cluster0.qtv2z.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", uuidRepresentation='standard')
db = client['enrollments']
enrollments = db['enrollments']
students = db['students']
admins = db['admins']
