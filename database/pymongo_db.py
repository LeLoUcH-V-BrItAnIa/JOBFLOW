from dotenv import load_dotenv
import os
from pymongo import MongoClient

# Loading dot env 
load_dotenv()

try:
    MONGO_URI = os.getenv("MONGO_URI")

    client = MongoClient(MONGO_URI)

    # database name 
    db = client["jobflow"]

    # creating tables 
    user_collection = db['user']
    job_collection = db['job']
except Exception as e:
    print(f"ERROR : {e}")
