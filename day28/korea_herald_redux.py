# Using Python and what you've learned so far, repeat the previous exercise and
# retrieve the "Most Popular" article headlines from the Korea Herald website.
# This time, use the BeautifulSoup package. Like before, list the headlines in
# the following format:
# [1]: Headline 1
# [2]: Headline 2
# [n]: Headline n
import requests
from bs4 import BeautifulSoup

herald_html = requests.get("https://koreaherald.com").text

soup = BeautifulSoup(herald_html, 'html.parser')
all_titles = [news.text for news in soup.select(".news_title")]

# For display
for idx, title in enumerate(all_titles):
    print(f"[{idx + 1}] {title}")
