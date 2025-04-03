from scrappers.implementation.primeit_scrapper import PrimeITScrapper
from fastapi import APIRouter, Query, Depends
import json

router = APIRouter()

@router.get("/jobs")
async def get_all_jobs():

    new_job = PrimeITScrapper()
    job_list = await new_job.run_scrapper()
    return json.dumps([crypto.dict() for crypto in job_list], indent=2)