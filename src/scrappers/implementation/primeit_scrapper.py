from scrappers.abstract.job_site_scrapper import JobSiteScrapper
from httpx import HTTPStatusError, RequestError
from scrappers.models.jobs_model import Job
from selectolax.parser import HTMLParser
from dotenv import load_dotenv
import asyncio
import httpx
import json
import os

load_dotenv()

class PrimeITScrapper(JobSiteScrapper):
    
    def __init__(self):
        self.website_url = ""
        self.scrapper_origin = "PrimeIT"
        self.collected_jobs = []
        self.raw_html = None
        self.current_page = 0

    async def get_website_data(self, retries=5, backoff_factor=1.0, timeout=10.0):
        """
        Fetch a URL with retries and exponential backoff.

        Args:
            url (str): The URL to fetch.
            retries (int): Number of retries before giving up.
            backoff_factor (float): Factor by which the wait time increases after each retry.
            timeout (float): Timeout for the request in seconds.

        Returns:
            str: The HTML content of the page if successful.

        Raises:
            Exception: If all retries fail.
        """

        for attempt in range(retries):
            try:
                async with httpx.AsyncClient(timeout=timeout) as client:
                    response = await client.get(self.website_url)
                    response.raise_for_status() 

                    self.raw_html = response.content
            except (HTTPStatusError, RequestError) as e:
                print(f"Attempt {attempt + 1}/{retries} failed: {e}")
                if attempt < retries - 1:
                    sleep_time = backoff_factor * (8 ** attempt)
                    print(f"Retrying in {sleep_time:.2f} seconds...")
                    await asyncio.sleep(sleep_time)
                else:
                    print("Max retries reached. Failing...")
                    raise

    async def generate_paginated_url(self) -> str:
        self.current_page += 1
        print(os.getenv("PRIMEIT_JOB_LISTING_BASE_URL") + "/page/" + str(self.current_page))
        if self.current_page == 1:
            return os.getenv("PRIMEIT_JOB_LISTING_BASE_URL")
        return os.getenv("PRIMEIT_JOB_LISTING_BASE_URL") + "/page/" + str(self.current_page)

    async def check_pagination_end(self, container):
        if container:
            has_children = any(child.tag is not None for child in container.iter())
            has_text = container.text(strip=True) != ""
            if not has_children and not has_text:
                return False
            return True

    async def parse_raw_html(self, parsed_data):
        if parsed_data:
            container = parsed_data.css_first("div.jobs-list-content")
            for job in container.css("article"):
                job_title_component = job.css_first("header > div.entrie-left > h4")
                job_description_component = job.css_first(".content-editor")
                job_link_component = job.css_first(".icon-circle-more")
                new_job = Job(
                    origin_company=self.scrapper_origin,
                    job_title=job_title_component.text(),
                    job_description=job_description_component.text(),
                    posted_date="None",
                    job_post_link=job_link_component.attributes["href"]
                )
                self.collected_jobs.append(new_job.model_dump())
        else:
            print("job container not found")

    async def run_scrapper(self):
        while True:
            self.website_url = await self.generate_paginated_url()
            await self.get_website_data()
            parser = HTMLParser(self.raw_html)
            container = parser.css_first("#start-carrers > div.width-medium.list-entries.z10 > div.jobs-list.active > div.jobs-list-content")
            if await self.check_pagination_end(container):
                await self.parse_raw_html(container)
            else:
                break
        return self.collected_jobs
