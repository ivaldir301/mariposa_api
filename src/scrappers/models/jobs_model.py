from pydantic import BaseModel

class Job(BaseModel):
    origin_company: str
    job_title: str
    job_description: str
    posted_date: str