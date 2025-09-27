# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 19:50:07 2025

@author: Lenovo
"""

from credential import x_api_key
import requests

def homestra_search(query):
  url = "https://piloterr.com/api/v2/homestra/search"

  querystring = {"query":query}
  headers = {"x-api-key": x_api_key}
  response = requests.get(url, headers=headers, params=querystring)
  #print(response.json())
  return response.json()

def website_crawler(site_url):
    url = "https://piloterr.com/api/v2/website/crawler"
    
    headers = {"x-api-key": x_api_key}
    querystring = {"query":site_url}
    
    response = requests.request("GET", url, headers=headers,params=querystring)
    
    # decode double escape "\\" and inline "\n" 
    clean_html = response.text.encode('utf-8').decode('unicode_escape')
    
    # decode special character 
    clean_html = clean_html.encode('latin-1').decode('utf-8')
   
    return clean_html

