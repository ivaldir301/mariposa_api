from abc import ABC, abstractmethod

class JobSiteScrapper(ABC):

    @abstractmethod
    async def get_website_data(website_url):
        pass

    @abstractmethod
    async def save():
        pass

    @abstractmethod
    async def run_scrapper():
       pass


