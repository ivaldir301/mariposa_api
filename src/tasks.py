from src.scrappers.implementation.primeit_scrapper import PrimeITScrapper
from asgiref.sync import async_to_sync
from src.celery_worker import celery
import asyncio

# app = Celery("mariposa_api")

# app.config_from_object("celery_config") 

@celery.task(name="src.tasks.run_primeit_scrapper")
def run_primeit_scrapper():
    scrapper = PrimeITScrapper()
    asyncio.run(scrapper.run_scrapper())

