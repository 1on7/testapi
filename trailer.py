from bs4 import BeautifulSoup
import requests
import json
def trailer(video_id):
        video_url = "https://www.imdb.com/video/"+           video_id
        print(video_url)

        r = requests.get(url=video_url)
        soup = BeautifulSoup(r.text, 'html.parser')
        script =soup.find("script",{'type': 'application/json'})
        json_object = json.loads(script.string)

        videos = json_object["props"]["pageProps"]["videoPlaybackData"]["video"]["playbackURLs"]
# links video quality order auto,1080,720
        vidFHd = videos[1]["url"]
        vidHd = videos[2]["url"]
        vidSd = videos[3]["url"]
        data = {'vidFHd':vidFHd, 'vidHd':vidHd, 'vidSd':vidSd}
        return json.dumps(data)