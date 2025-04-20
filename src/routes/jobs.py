from repository.database.services.job_service import get_all_jobs_from_db
from scrappers.implementation.primeit_scrapper import PrimeITScrapper
from fastapi import APIRouter

router = APIRouter()

@router.get("/jobs")
async def get_all_jobs():
    job_list = await get_all_jobs_from_db()
    return job_list