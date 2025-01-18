from flask import Flask, jsonify, request
from pymongo import MongoClient
import os
from dotenv import load_dotenv

app = Flask(__name__)
# Get API_KEY from environment variable
API_KEY = "1d67bad29c76451bf695248c9db0ae15e8d4226835287bbe2532e20600de3eb8"

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["education_db"]
colleges_collection = db["colleges"]

# Function to check API key in request headers
def check_api_key():
    api_key = request.headers.get("API-Key")
    if api_key != API_KEY:
        return jsonify({"error": "Unauthorized access, invalid API key"}), 403
    return None

@app.route("/colleges", methods=["GET"])
def get_colleges():
    # Check for valid API key in the request headers
    auth_error = check_api_key()
    if auth_error:
        return auth_error
    
    # Fetch colleges from MongoDB
    colleges = list(colleges_collection.find({}, {"_id": 0}))  # Exclude MongoDB _id field
    return jsonify(colleges)

if __name__ == "__main__":
    app.run(debug=True)