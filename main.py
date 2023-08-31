import json
from dotenv import load_dotenv
import os
from address_finder import AddressFinder
from volume_finder import VolumeFinder
from scraper import Scrape
import asyncio

scraper = Scrape

# async def scrape_data(date):  # date argument added
#     if date or not date: 
#         print(f"Scraping data for date: {date}")

#     url = os.getenv("PROVANS_WEBSITE")
#     scraper = Scrape(url, date)
#     return await scraper.scrape_orders()

# loop = asyncio.get_event_loop()
# data = loop.run_until_complete(scrape_data("2023-08-31"))

load_dotenv()

google_maps_api_key = os.getenv("GOOGLE_MAPS_API")

def read_database_file():
    with open('all_orders2.json', 'r') as f:
        return json.load(f)

api_key = google_maps_api_key
database_jobs = read_database_file()

# job_formatter = AddressFinder(api_key)
# database_jobs = job_formatter.format_job_details(database_jobs)

volume_finder = VolumeFinder(database_jobs)
formatted_details = volume_finder.get_updated_jobs()
volume_finder.save_to_file()

# print(formatted_details)





# update address_finder so it is like volume finder. add total volume to order.
# need to work out insulation