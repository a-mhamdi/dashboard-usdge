from pymongo import MongoClient
from bson import ObjectId

import os

from dotenv import load_dotenv
load_dotenv()


def find_documents_by_data(nature, date, enseignant):

    jury = "jury" + nature

    try:
        # Connect to MongoDB
        client = os.getenv("DATABASE_URL")
        db_name = os.getenv("DB_NAME")
        collection_name = os.getenv("COLLECTION_NAME")
        client = MongoClient(client)
        # Access the database and collection
        db = client[db_name]
        collection = db[collection_name]

        # Query documents
        query = {
            "submissionDate": date,
            "$or": [
                {f"{jury}.jury1": enseignant},
                {f"{jury}.jury2": enseignant}
            ]
        }
        projection = {"_id": 1}  # Only return _id field

        # Execute query and extract _id values
        cursor = collection.find(query, projection)
        id_list = [str(doc["_id"]) for doc in cursor]

        return id_list

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

    finally:
        client.close()
