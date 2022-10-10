from bs4 import BeautifulSoup
import requests
import json
def data_info(uid):
        url = 'https://m.imdb.com/title/'+uid

        response = requests.get(url)

        list = []

        soup = BeautifulSoup(json.loads(response.content), 'html.parser')

        data = {};
        title = soup.find('h1', class_ ='sc-b73cd867-0 eKrKux').text
        year = soup.find('span', class_ ='sc-8c396aa2-2 itZqyK').text
        run_time = soup.find_all(class_ = 'ipc-inline-list__item')[5].text
        description = soup.find(class_ = 'sc-16ede01-0 fMPjMP').text
        json_list = soup.find_all('script')[1].text
        json_data = json.loads(json_list)
        genre = json_data['genre']
        try:
            meta_score = soup.find('span', 'score-meta').text
        except:
                meta_score = ""
                try :
                   critic_reviews = soup.find_all('span', 'score')[1].text
                except:
                   	critic_reviews = ""
        reviews = soup.find_all('span', 'score')[0].text
        oscars = soup.find_all('a', 'ipc-metadata-list-item__label ipc-metadata-list-item__label--link')[4].text
        poster = soup.find_all('meta')[9]['content']
        try :
           age = soup.find_all('span', class_ = 'sc-8c396aa2-2 itZqyK')[1].text
        except:
        	age = ""
        data = {'title':title, 'poster':poster, 'year':year, 'age':age,'time':run_time, 'genre':genre, 'description':description, 'meta_score':meta_score, 'critic_reviews':critic_reviews, 'reviews':reviews, 'oscars':oscars}
        list.append(data)
        json_dump = json.dumps(list)
        return json_dump
