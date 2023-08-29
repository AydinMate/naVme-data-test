import json
from dotenv import load_dotenv
import os
from address_finder import AddressFinder
from volume_finder import VolumeFinder

load_dotenv()

google_maps_api_key = os.getenv("GOOGLE_MAPS_API")

def read_database_file():
    with open('all_orders.json', 'r') as f:
        return json.load(f)

api_key = google_maps_api_key
database_jobs = read_database_file()

# volume_finder = VolumeFinder(database_jobs)
# formatted_details = volume_finder.get_updated_jobs()
# volume_finder.save_to_file()

# print(formatted_details)


job_formatter = AddressFinder(api_key)
database_jobs = job_formatter.format_job_details(database_jobs)

print(database_jobs)


# update address_finder so it is like volume finder.