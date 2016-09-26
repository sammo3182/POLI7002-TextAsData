import requests
url = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?fq=obamacare&page=1&begin_date=20160101&end_date=20161231&api-key=2b621b40460346d889170e2acb66f636'
response = requests.get(url)
data = response.json()
