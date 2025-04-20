from repository.database.services.job_service import create_raw_job
from implementation.primeit_scrapper import PrimeITScrapper
from celery_worker import celery

@celery.task
async def run():
    scrapper = PrimeITScrapper(
        website_url="https://www.primeit.pt/en/careers#start-carrers"
    )

    await create_raw_job(await scrapper.run_scrapper())
