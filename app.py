from flask import Flask, jsonify
from pymongo import MongoClient
import os
app = Flask(__name__)
# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
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
@app.route("/colleges", methods=["GET"])
def get_colleges():
    """Fetch and return the list of colleges."""
    colleges = list(colleges_collection.find({}, {"_id": 0}))  # Exclude the MongoDB `_id` field
    return jsonify(colleges)
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.getenv("PORT", 5000)))