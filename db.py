from pymongo import MongoClient

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")

# Database and collection
db = client["education_db"]
colleges_collection = db["colleges"]

# Sample college data in JSON format
colleges_data = [
    {"name": "Harvard University", "location": "Cambridge, MA", "rank": 1},
    {"name": "Stanford University", "location": "Stanford, CA", "rank": 2},
    {"name": "MIT", "location": "Cambridge, MA", "rank": 3},
    {"name": "University of Oxford", "location": "Oxford, UK", "rank": 4},
]

# Insert the data into the collection (only if it's empty)
if colleges_collection.count_documents({}) == 0:
    colleges_collection.insert_many(colleges_data)

print("Data inserted successfully!")