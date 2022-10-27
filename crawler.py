
from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pandas as pd
import xlwt
import openpyxl
    
def req():
    url = 'https://www.finn.no/realestate/homes/search.html?location=1.22046.20220&sort=PUBLISHED_DESC'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='__next')
    listings = results.find_all('article', class_ = 'relative overflow-hidden transition-all outline-none sf-ad-outline sf-ad-card rounded-8 mt-24 mx-16 mb-16 sm:mb-24 relative')
    titles = []
    addys = []
    sq_prices = []
    for listing in listings:
        title = listing.find('h2', class_='col-span-2 mt-12 sm:mt-24 mb-0 h4')
        addy = listing.find('div', class_='sm:order-first sm:text-right mt-4 sm:mt-0 sm:ml-16 sf-line-clamp-2 sf-realestate-location')
        sq_price = listing.find('div', class_='col-span-2 mt-16 sm:mt-4 flex justify-between sm:block space-x-12 font-bold')
        titles.append(title.text.strip())
        addys.append(addy.text.strip())
        sq_prices.append(sq_price.text.strip())
    df = pd.DataFrame({'Address' : addys, 'Sqm and price' : sq_prices})
    df.to_excel('listings.xlsx', index=False, encoding='utf-8')
    return
    
print(req())