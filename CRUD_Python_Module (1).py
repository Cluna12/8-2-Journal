from typing import List, Dict, Any
from pymongo import MongoClient
from pymongo.errors import PyMongoError
import os

class AnimalShelter:
    """
    CRUD operations for the 'animals' collection in the 'aac' database.
    Authenticate with Mongo using aacuser credentials.
    """

    def __init__(
        self,
        username: str = "aacuser",
        password: str | None = None,
        host: str = "127.0.0.1",
        port: int = 27017,
        auth_db: str = "admin",
        db: str = "aac",
        col: str = "animals",
    ):
        if password is None:
            password = os.environ.get("AAC_PWD", "")

        self.client = MongoClient(
            host=host,
            port=port,
            username=username,
            password=password,
            authSource=auth_db,
            serverSelectionTimeoutMS=5000,
        )
        self.client.admin.command("ping")
        self.database = self.client[db]
        self.collection = self.database[col]

    # Create
    def create(self, data: Dict[str, Any]) -> bool:
        if not isinstance(data, dict) or not data:
            return False
        try:
            res = self.collection.insert_one(data)
            return bool(res.inserted_id)
        except PyMongoError:
            return False

    # Read
    def read(self, query: Dict[str, Any]) -> List[Dict[str, Any]]:
        if not isinstance(query, dict):
            return []
        try:
            return list(self.collection.find(query))
        except PyMongoError:
            return []

    # Update
    def update(self, query: Dict[str, Any], new_values: Dict[str, Any]) -> int:
        if not isinstance(query, dict) or not isinstance(new_values, dict):
            return 0
        try:
            result = self.collection.update_many(query, {"$set": new_values})
            return result.modified_count
        except PyMongoError:
            return 0

    # Delete
    def delete(self, query: Dict[str, Any]) -> int:
        if not isinstance(query, dict):
            return 0
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except PyMongoError:
            return 0
