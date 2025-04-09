from implementation.primeit_scrapper import PrimeITScrapper
import json

async def run():
    scrapper = PrimeITScrapper(
        website_url="https://www.primeit.pt/en/careers#start-carrers"
    )

    return await json.dumps(scrapper.run_scrapper())


