import giphy_client
from giphy_client.rest import ApiException

api_instance = giphy_client.DefaultApi()
api_key = 'ggVgktjnMfuZ1wjMouSrudAbHBcJJz0V'
query = 'chad sigma'
limit = 5

try:
    response = api_instance.gifs_search_get(api_key, query, limit=limit)
    for gif in response.data:
        print(gif.url)
except ApiException as e:
    print(f"API exception: {e}")
