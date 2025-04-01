from fastapi import APIRouter, Query, Depends
from scrappers.implementation.delloite_scrapper import DelloitteScrapper

router = APIRouter()

@router.get("/jobs")
def get_all_jobs():

    new_job = DelloitteScrapper()
    return new_job.run_scrapper()