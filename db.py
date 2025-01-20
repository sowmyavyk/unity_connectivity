from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)

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