# db.py
import motor.motor_asyncio
import os

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URI)

db = client["your_database_name"]
collection = db["raw_jobs"]
