from newsapi import NewsApiClient
import config

newsapi = NewsApiClient(api_key=config.NEWS_API_KEY)

response = newsapi.get_everything(q='Apple', page_size=5)
print(response['articles'][0])