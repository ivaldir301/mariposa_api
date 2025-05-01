# db.py
import os
import certifi
from dotenv import load_dotenv
import motor.motor_asyncio
from pymongo.server_api import ServerApi

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

client = motor.motor_asyncio.AsyncIOMotorClient(
    MONGODB_URI,
    server_api=ServerApi('1'),           
    tls=True,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=20000,
)

db = client["mariposa"]
collection = db["raw_jobs"]
