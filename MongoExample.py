# robo 3T

# mongodb extension for VSCode

# create a "stream_tracker" database
# create a collection named "streams"


import pymongo

client = pymongo.MongoClient("mongodb://admin:admin@localhost:27017")

db = client.stream_tracker  # get database
stream_collection = db.streams

# insert some stuff
stream_data = {
    "channel_id": "blah",
    "channel_name": "blah blah",
    "tags": ["one", "two", "three"],
    "nested": {"stuff": "in it"},
}
stream_collection.insert_one(stream_data)
