import pymongo
import CONFIG
client = pymongo.MongoClient(CONFIG.mongodbURI)
db = client["neuralflow"]
UsersDB = db["users"]