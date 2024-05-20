# import requests

# res = requests.get("https://google.com").text
# print(res)

# r = requests.get('https://dog.ceo/api/breeds/list/all')
# all_breeds = r.json()
# print(all_breeds)

# from bs4 import BeautifulSoup

# browser_spoof = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# r = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250', headers=browser_spoof)
# soup = BeautifulSoup(r.text, 'html.parser')

# movies = soup.select('li.ipc-metadata-list-summary-item')

# for movie in movies[:10]:
#   movie_title = movie.select_one('.ipc-title__text').text
#   print(movie_title)

# https://query1.finance.yahoo.com/v7/finance/quote?&symbols=AAPL,AMD,AMZN,BABA,CLSK,DNN,GME,HOOD,INTC,KVUE,MARA,NIO,NVDA,PLTR,PLUG,SOFI,TSLA&fields=currency,fromCurrency,toCurrency,exchangeTimezoneName,exchangeTimezoneShortName,gmtOffSetMilliseconds,regularMarketChange,regularMarketChangePercent,regularMarketPrice,regularMarketTime,preMarketTime,postMarketTime,extendedMarketTime&crumb=Iqlu0aZZRQb&formatted=false&region=US&lang=en-US

import requests
from bs4 import BeautifulSoup

herald_html = requests.get("https://finance.yahoo.com/most-active/?offset=0&count=100&guccounter=1").text

soup = BeautifulSoup(herald_html, 'html.parser')
table = soup.select("#scr-res-table table tbody tr")

for row in table:
    try:
        name = row.select_one('td[aria-label="Name"]').text
        price = row.select_one("td[aria-label='Price (Intraday)']").text
        change = row.select_one("td[aria-label='Change'] fin-streamer span").text
        print(f"{name}\t${price}\t{change}%")
    except AttributeError as e:
        print("CAUGHT: ", e)