from bs4 import BeautifulSoup
import requests
import json
def data_search(title):
        url = 'https://m.imdb.com/find?q='+title+'&s=tt&exact=true&ref_=fn_tt_ex'

        response = requests.get(url)

        list = []

        soup = BeautifulSoup(response.content, 'html.parser')
        store = soup.find_all('script')[59].text
        data = json.loads(store)
        data = data['props']['pageProps']['titleResults']['results']
        for x in data:
               title = x['titleNameText']
               try :
                   poster = x['titlePosterImageModel']['url']
               except :
               	poster = ''
               year = x['titleReleaseText'].replace('\u2013', '')
               type = x['imageType']
               data = {'title':title, 'poster':poster, 'year':year, 'type':type}
               list.append(data)
               json_dump = json.dumps(list)
        return json_dump