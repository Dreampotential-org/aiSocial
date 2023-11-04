import pymongo


url = 'mongodb://localhost:27017'
client = pymongo.MongoClient(url)
db = client['mydattabase']
collection = db['new7']

# Custom JSON encoder for handling ObjectId serialization
