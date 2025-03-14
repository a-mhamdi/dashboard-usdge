from pymongo import MongoClient
from bson import ObjectId


def find_documents_by_data(nature, date, enseignant):
    """
    Find documents where Data field matches a specific value and return their _id fields

    Parameters:
    connection_string (str): MongoDB connection string
    database_name (str): Name of the database
    collection_name (str): Name of the collection
    data_value: Value to match in the Data field

    Returns:
    list: List of _id values from matching documents
    """

    jury = "jury" + nature

    try:
        # Connect to MongoDB
        client = MongoClient("mongodb://localhost:27017/connection_string")
        db = client["dept-ge"]
        collection = db["students"]

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
