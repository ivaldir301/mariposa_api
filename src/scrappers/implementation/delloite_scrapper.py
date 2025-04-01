from scrappers.abstract.job_site_scrapper import JobSiteScrapper
from scrappers.models.jobs_model import Job

class DelloitteScrapper(JobSiteScrapper):

    def run_scrapper(self):
        new_job = Job(
            origin_company="PrimeIT",
            job_title="Best programmer in the world",
            job_description="you have to be like Alan Turing",
            posted_date="01/04/2025"
        )

        return new_job

