import requests
from bs4 import BeautifulSoup
import json

url = 'https://m.imdb.com/list/ls073877946/'

response = requests.get(url)

list = []

soup = BeautifulSoup(response.content, 'html.parser')

movie_data = soup.findAll('div', attrs= {'class': 'col-xs-12 col-md-6 lister-item mode-simple'})
for store in movie_data:
       img_list = store.find("img")
       movieTitle = img_list.get("alt")
       poster = img_list.get("data-src-x2")
       id = img_list.get("data-tconst")
       year = store.find('span', class_ = "nowrap").text
       time = store.p.find('span', class_ = "runtime").text
       ratings = store.p.find('span', class_ ="genre").text.replace('\n', "").replace(' ', "")
       rating = store.find('span', class_ ="imdb-rating").text
       data = {'poster':poster, 'name':movieTitle, 'id':id, 'year':year, 'Time':time, 'Ratings':ratings, 'Rating':rating}
       list.append(data)
       json_dump = json.dumps(list)
       return json_dump
