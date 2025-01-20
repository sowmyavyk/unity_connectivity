from flask import Flask, jsonify
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# MongoDB connection using Atlas
MONGO_URI = os.getenv("MONGO_URI")  # Get MongoDB URI from environment variables
client = MongoClient(MONGO_URI)
db = client["education_db"]
colleges_collection = db["colleges"]

# Insert sample data (only if the collection is empty)
if colleges_collection.count_documents({}) == 0:
    sample_colleges = [
        {"name": "Harvard University", "location": "Cambridge, MA", "rank": 1},
        {"name": "Stanford University", "location": "Stanford, CA", "rank": 2},
        {"name": "MIT", "location": "Cambridge, MA", "rank": 3},
        {"name": "University of Oxford", "location": "Oxford, UK", "rank": 4},
    ]
    colleges_collection.insert_many(sample_colleges)
    print("Inserted sample data")
else:
    print("Data already exists")

@app.route("/colleges", methods=["GET"])
def get_colleges():
    """Fetch and return the list of colleges."""
    colleges = list(colleges_collection.find({}, {"_id": 0}))  # Exclude the MongoDB `_id` field
    return jsonify(colleges)

if __name__ == "__main__":
    # Ensure the app binds to the correct port
    app.run(debug=True, host="0.0.0.0", port=int(os.getenv("PORT", 5001)))