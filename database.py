
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
load_dotenv()

print(os.getenv("DB_NAME"))
print(os.getenv("DB_PASSWORD"))

uri = f"mongodb+srv://{os.getenv("DB_NAME")}:{os.getenv("DB_PASSWORD")}@crud-person.rm6bg.mongodb.net/?appName=crud-person"
print(uri)
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.get_database("studyRat")
activityCollection = db.get_collection("activity")


# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)