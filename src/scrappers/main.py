from implementation.primeit_scrapper import PrimeITScrapper

async def run():
    scrapper = PrimeITScrapper(
        website_url="https://www.primeit.pt/en/careers#start-carrers"
    )

    return await scrapper.run_scrapper()


