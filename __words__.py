from datetime import datetime
import time
import re
import requests
from bs4 import BeautifulSoup


def fetch_xml(country_code="KR"):
    url = f"https://trends.google.com/trends/trendingsearches/daily/rss?geo={country_code}"
    start = time.time()
    response = requests.get(url)
    response_time = time.time() - start
    print(f"The request took {response_time}s to complete.")
    return response.content


def trends_retriever(country_code='KR'):
    xml_document = fetch_xml(country_code)
    soup = BeautifulSoup(xml_document, "lxml")
    titles = soup.find_all("title")
    approximate_traffic = soup.find_all("ht:approx_traffic")
    approximate_date = soup.find_all("pubdate")
    ans = [(title.text, re.sub("[+,]", "", traffic.text),
            datetime.strptime(' '.join(timeline.text.split()[:4]), '%a, %d %b %Y').strftime('%Y_%m_%d'))
           for title, traffic, timeline
           in zip(titles[1:], approximate_traffic, approximate_date)]
    return ans


def read_word(lang):
    if lang == 'kr':
        path = "./source/my_kr_word.txt"
    elif lang == 'en':
        path = './source/my_en_word.txt'
    with open(path) as f:
        words = f.read().splitlines()
    return words


def trend_writer(trends,lang):
    daily_trend = [i[0] for i in trends]
    with open(f'source/my_{lang}_word.txt', 'w') as file:
        for trend in daily_trend:
            file.write(trend + '\n')
    file.close()
    return None
