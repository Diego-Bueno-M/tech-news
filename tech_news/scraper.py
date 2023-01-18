import requests
import time
from parsel import Selector
from bs4 import BeautifulSoup
import re


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    header = {"user-agent": "Fake user-agent"}
    try:
        response = requests.get(url, headers=header, timeout=3)
        time.sleep(1)
        if (response.status_code == 200):
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""
    urlsList = []
    selector = Selector(text=html_content)
    url = selector.css(".entry-header h2 a::attr(href)").getall()
    urlsList.extend(url)
    return urlsList


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    url = selector.css(".next::attr(href)").get()
    return url


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)

    url = selector.css("link[rel=canonical]::attr(href)").get()

    title = selector.css("h1.entry-title::text").get().strip()

    timestamp = selector.css(".meta-date::text").get()

    writer = selector.css(".author a::text").get()

    comments_count = selector.css("h5.title-block::text").get()
    comments_count = re.sub('[^0-9]', '', comments_count)

    if comments_count == '':
        comments_count = 0

    summary = selector.css(".entry-content p").get()
    soup = BeautifulSoup(summary, 'html.parser')

    tags = selector.css(".post-tags a::text").getall()

    category = selector.css(".label::text").get()

    newInfo = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": soup.get_text().strip(),
        "tags": tags,
        "category": category,
    }
    return newInfo


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
