# -*- coding: utf-8 -*-

from script.piloterr import website_crawler, homestra_search
from script.homestra import get_summary, get_detailed_information, query_builder
from bs4 import BeautifulSoup
from tqdm import tqdm

## SCRAP SEARCH RESULT

MAX_PAGE = 1

parcels = []
for i in tqdm(range(1,MAX_PAGE+1)):
  print(query_builder(page=i))
  query = query_builder(page=i,country=None)   # country=None means no filter on country, all properties found will be returned !
  parcels.extend(homestra_search(query))

print(f"\n> {len(parcels)} Homestra properties scraped ! ")

## OPEN Each Property and LOAD summary, detailed data 
for parcel in tqdm(parcels):

    ### SCRAPE PROPERTY DETAIL
    query = "https://homestra.com/property/" + parcel["slug"]
    print(f"\n\nScraping more information from {query}")
    response_html = website_crawler(query)

    ### EXTRACT DETAIL
    soup = BeautifulSoup(response_html, 'html.parser')

    summary = get_summary(soup)
    detail = get_detailed_information(soup)

    parcel["summary"] = summary
    parcel["detail"] = detail