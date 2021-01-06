# https://splinter.readthedocs.io/en/latest/drivers/chrome.html
from splinter import Browser
from bs4 import BeautifulSoup

browser = Browser('chrome', headless=False)
url = 'http://books.toscrape.com/'
browser.visit(url)

# Iterate through all pages
for x in range(50):
    # HTML object
    html = browser.html
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all elements that contain book information
    articles = soup.find_all('article', class_='product_pod')

    # Iterate through each book
    for article in articles:
        # Use Beautiful Soup's find() method to navigate and retrieve attributes
        h3 = article.find('h3')
        link = h3.find('a')
        href = link['href']
        title = link['title']
        print('-----------')
        print(title)
        print('http://books.toscrape.com/' + href)

# Click the 'Next' button on each page
browser.click_link_by_partial_text('next')
