from src.repository.database.models import DynamicModel
from src.repository.database.db import collection
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
from bson import ObjectId

async def create_raw_job(job: DynamicModel) -> dict:
    job_dict = jsonable_encoder(job)
    result = await collection.insert_one(job_dict)
    return {
        "id": str(result.inserted_id)
    }

async def get_raw_job(job_id: str):
    if not ObjectId.is_valid(job_id):
        return HTTPException(status_code=400, detail="Invalid job ID format")
    job = await collection.find_one({"_id": ObjectId(job_id)})
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return jsonable_encoder(job)

def fix_object_id(doc):
    doc['_id'] = str(doc['_id'])
    return doc

async def get_all_jobs_from_db() -> list:
    jobs = []
    cursor = collection.find()
    async for job in cursor:
        jobs.append(fix_object_id(job))
    return jobs

async def check_if_job_exists(job_title: str, job_description: str):
    job = await collection.find_one({
        "job_title": job_title,
        "job_description": job_description
        }
    )
    if job is None:
            return None
    return job