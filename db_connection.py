import pymongo


url = 'mongodb://localhost:27017'
client = pymongo.MongoClient(url)
db = client['mydattabase']
collection = db['new9']

# Custom JSON encoder for handling ObjectId serialization
