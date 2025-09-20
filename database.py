from pymongo import MongoClient

# Example: local MongoDB (default port 27017)
client = MongoClient("mongodb://localhost:27017/")
# select database
db = client["sports_academy"]