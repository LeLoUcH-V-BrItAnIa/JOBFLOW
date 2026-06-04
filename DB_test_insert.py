from pymongo import MongoClient
import os

uri = "mongodb+srv://kaustav_60:ironmantonystark100@firstcluster0.n2txixc.mongodb.net/?appName=FirstCluster0"
client = MongoClient(uri)

DB = client["jobflow"]
collection = DB["test"]

data = {
    "name":"kaustav",
    "status":"connected"
}
collection.insert_one(data)

print("Inserted Successfully!")