# -*- coding: utf-8 -*-

from script.piloterr import website_crawler, homestra_search
from script.homestra import get_summary, get_detailed_information, query_builder
from bs4 import BeautifulSoup
from tqdm import tqdm
import json
import os


'''
 Step 1. Scrape Homestra properties with the Piloterr API
 
'''
MAX_PAGE = 2    # set the number of pages to scrape

parcels = []
for i in tqdm(range(1,MAX_PAGE+1)):
  print(query_builder(page=i))
  query = query_builder(page=i,country=None)   # country=None means no filter on country, all properties found will be returned !
  parcels.extend(homestra_search(query))

print(f"\n> {len(parcels)} Homestra properties scraped ! ")

'''
 Step 2. Enrich data using the Piloterr Website Crawler
 
'''
for parcel in tqdm(parcels):
    # Open Property Link and Scrape HTML
    query = "https://homestra.com/property/" + parcel["slug"]
    print(f"\n\nScraping more information from {query}")
    response_html = website_crawler(query)
    soup = BeautifulSoup(response_html, 'html.parser')
    
    # Add Scrape Data to the main data
    parcel["summary"] = get_summary(soup)
    parcel["detail"] = get_detailed_information(soup)



'''
 Step 3. Saving the Dataset into A json file
 
'''
# Create the output directory if it doesn't exist
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Define the output file path
output_file = os.path.join(output_dir, "homstra_preperties_listing.json")

# Write the parcels data to the JSON file
with open(output_file, "w") as f:
    json.dump(parcels, f, indent=4)

print(f"Successfully exported {len(parcels)} parcels to {output_file}")

