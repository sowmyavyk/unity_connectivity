from flask import Flask, jsonify, request
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)

# Get API_KEY from environment variable
API_KEY = os.getenv("API_KEY")

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
    app.run(debug=True, host="0.0.0.0", port=int(os.getenv("PORT", 5000)))