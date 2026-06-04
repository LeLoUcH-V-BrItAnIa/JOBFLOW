from pymongo import MongoClient
import os

uri = "mongodb+srv://kaustav_60:ironmantonystark100@firstcluster0.n2txixc.mongodb.net/?appName=FirstCluster0" or os.getenv("MONGO_URI")

try:
    client = MongoClient(uri, serverSelectionTimeoutMS=5000)
    print(client.admin.command("ping"))
    print("CONNECTED")
except Exception as e:
    print("ERROR:")
    print(e)