from abc import ABC, abstractmethod

class JobSiteScrapper(ABC):

    @abstractmethod
    def get_website_data(website_url):
        pass

    @abstractmethod
    def run_scrapper():
       pass

