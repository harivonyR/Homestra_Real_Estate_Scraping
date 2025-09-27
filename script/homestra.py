# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 19:46:30 2025

@author: Lenovo
"""

def query_builder(country=None,max_price="no_max",min_price="no_min",page=1):
  if country :
    return f"https://homestra.com/list/houses-for-sale/{country}/?maximum-price={max_price}&minimum-price={min_price}&page={page}"
  else :
    return f"https://homestra.com/list/houses-for-sale/?maximum-price={max_price}&minimum-price={min_price}&page={page}"

## a - summary information
def  get_summary(soup):
    elements = soup.select('.text-gray-800.font-medium')

    summary_information = []
    for element in elements :
        info_text = element.text.strip()
        summary_information.append(info_text)

    print(f"[Summary] : {summary_information}")
    return summary_information

## b - detail information
def get_detailed_information(soup):

    elements = soup.select('div.py-4.sm\\:py-5.sm\\:grid > dt')

    detailed_information = {}
    for element in elements:
        # set the tag <dt> as key
        key = element.text.strip()

        # the next <dd> element is the value
        value_element = element.find_next_sibling('dd')

        # handle the case we didn't found any next element
        if value_element:
            value = value_element.text.strip()
        else:
            value = "#N/A"

        detailed_information[key] = value

        print(f"[detail] {key} = {value}")
        #print("\n\n")

    return detailed_information