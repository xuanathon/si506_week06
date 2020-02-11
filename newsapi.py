
import requests
import secrets



base_url = 'https://newsapi.org/v2/top-headlines'
params = {
    "q": "new hampshire",
    "apiKey": secrets.NEWSAPI_KEY
}

response = requests.get(base_url, params)
result = response.json()

for article in result["articles"]:
    print(f'{article["title"]} ({article["source"]["name"]})')
