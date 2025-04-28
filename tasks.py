from src.scrappers.implementation.primeit_scrapper import PrimeITScrapper
from asgiref.sync import async_to_sync
from celery import Celery


app = Celery("mariposa_api")
# app.config_from_object("celery_config") 

@app.task(name="src.tasks.run_primeit_scrapper")
def run_primeit_scrapper():
    scrapper = PrimeITScrapper()
    async_to_sync(scrapper.run_scrapper())

