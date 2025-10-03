import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")
MONGODB_DATABASE = os.getenv("MONGODB_DATABASE")
MONGODB_COLLECTION = os.getenv("MONGODB_COLLECTION")

# Conecta ao MongoDB
client = MongoClient(MONGODB_URL)

db = client[MONGODB_DATABASE]

collection_name = db[MONGODB_COLLECTION]