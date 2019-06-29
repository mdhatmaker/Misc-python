import json, urllib
APP_ID = 'YahooDemo' # Change this to your API key
SEARCH_BASE = "http://search.yahooapis.com/WebSearchService/V1/webSearch"

class YahooSearchError(Exception):
    pass

def search(query, results=20, start=1, **kwargs):
    kwargs.update({
        'appid': APP_ID,
        'query': query,
        'results': results,
        'start': start,
        'output': 'json'
    })
    url = SEARCH_BASE + '?' + urllib.urlencode(kwargs)
    result = json.load(urllib.urlopen(url))
    if 'Error' in result:
        # An error occurred; raise an exception
        raise YahooSearchError, result['Error']
    return result['ResultSet']
