# https://splinter.readthedocs.io/en/latest/drivers/chrome.html
from splinter import Browser
from bs4 import BeautifulSoup

browser = Browser('chrome', headless=False)
url = 'http://books.toscrape.com/'
browser.visit(url)

html = browser.html
soup = BeautifulSoup(html, 'html.parser')

sidebar = soup.find('ul', class_='nav-list')

categories = sidebar.find_all('li')

category_list = []
url_list = []
book_url_list = []
for category in categories:
    title = category.text.strip()
    category_list.append(title)
    book_url = category.find('a')['href']
    url_list.append(book_url)

book_url_list = ['http://books.toscrape.com/' + url for url in url_list]

titles_and_urls = zip(category_list, book_url_list)

for title_url in titles_and_urls:
    browser.click_link_by_partial_text('next')
