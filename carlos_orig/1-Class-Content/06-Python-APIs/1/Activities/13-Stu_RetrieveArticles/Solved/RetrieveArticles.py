# Dependencies
import requests as req

url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?"
api_key = "164b73c522a8420c8e05343ef1da0a7e"

# Store a search term
q = "obama"

# Search for articles published between a begin and end date
begin_date = "20160101"
end_date = "20160130"

query = url + "api-key=" + api_key + "&q=" + q + "&begin_date=" + begin_date\
    + "&end_date=" + end_date

# Retrieve articles
articles = req.get(query).json()
_articles = [article for article in articles["response"]["docs"]]

for article in _articles:
    print("A snippet from the article: '" + article["snippet"] + "'.\n")

# BONUS: How would we get 30 results? HINT: Look up the page query param
_articles = []
for page in range(1, 3):
    query = query + "&page=" + str(page)
    articles = req.get(query).json()
    _articles.extend([article for article in articles])
