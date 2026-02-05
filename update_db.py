#!.venv/bin/python

import csv
import os

from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

# MongoDB connection
client = MongoClient(os.getenv("MONGO_URI_DEV"))
db = client[os.getenv("MONGO_DATABASE")]
collection = db[os.getenv("MONGO_COLLECTION")]

# Define the key to match on (not _id)
match_key = "cin"

# Read CSV and update records
with open("data.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        query = {match_key: row[match_key]}
        update = {"$set": row}
        # upsert=True inserts if not found
        collection.update_one(query, update, upsert=True)
