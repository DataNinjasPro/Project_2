# Dependencies
import requests as req
from api_keys import nyt_api_key

url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?"
api_key = nyt_api_key

# Search for articles that mention granola
q = "granola"

# Build query URL
query = url + "api-key=" + api_key + "&q=" + q

# Populate articles
articles = req.get(query).json()

# The "response" property in articles contains the actual articles
# list comprehension.
_articles = [article for article in articles["response"]["docs"]]

# Proof articles stored
print("Your Reading List\n")
for article in _articles:
    print(article["web_url"])
