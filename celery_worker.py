from dotenv import load_dotenv
from celery import Celery
import os

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery = Celery(
    "mariposa",
    broker=REDIS_URL,
    backend=REDIS_URL
)

celery.conf.beat_schedule = {
    "run-scraper-every-30-minutes": {
        "task": "src.tasks.run_primeit_scrapper",
        "schedule": 300.0,
    }
}

celery.autodiscover_tasks(["src"])
