from flask import Flask, jsonify, request
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["education_db"]
colleges_collection = db["colleges"]

# API Key
API_KEY = os.getenv("API_KEY")

def check_api_key():
    """Check if the API key in the request headers is valid."""
    api_key = request.headers.get("API-Key")
    if api_key != API_KEY:
        return jsonify({"error": "Unauthorized access, invalid API key"}), 403
    return None

@app.route("/colleges", methods=["GET"])
def get_colleges():
    """Fetch and return the list of colleges."""
    # Check for valid API key in the request headers
    auth_error = check_api_key()
    if auth_error:
        return auth_error

    colleges = list(colleges_collection.find({}, {"_id": 0}))  # Exclude the MongoDB `_id` field
    return jsonify(colleges)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.getenv("PORT", 5001)))