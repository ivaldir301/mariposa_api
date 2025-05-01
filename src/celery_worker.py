from dotenv import load_dotenv
from celery import Celery
import os

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery = Celery(
    "mariposa",
    broker=REDIS_URL,
    backend=REDIS_URL,
    include=["src.tasks"]
)

# after your celery = Celery(...) block
celery.conf.enable_utc = True
celery.conf.timezone = "Europe/Lisbon"  # or "UTC" if you prefer

celery.conf.beat_schedule = {
    "run-scraper-every-5-minutes": {
        "task": "src.tasks.run_primeit_scrapper",
        "schedule": 120.0  
    }
}

celery.autodiscover_tasks(["src"])