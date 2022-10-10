from flask import *
import requests
from bs4 import BeautifulSoup
import schedule as s
import threaded
import time as t
import _thread as thread
from trailer import trailer
import json
from info import data_info
from movies import movie
app = Flask(__name__)
def rescrap():
        from movies import movie
        return movie()
def ref():
        s.every().day.at("12:00").do(rescrap)
        while True:
                     s.run_pending()
                     t.sleep(1)
thread.start_new_thread(ref, ())
@app.route("/movie", methods=['POST', 'GET'])
def movies():
        return movie()
@app.route("/info", methods=['POST', 'GET'])
def info():
      uid = str(request.args.get('id'))
      return data_info(uid)
@app.route("/search/", methods=['POST', 'GET'])
def search():
      name = str(request.args.get('name'))
      data = {'name' : name}
      return data
@app.route("/trailer/", methods=['POST', 'GET'])
def tr():
	video_id = str(request.args.get('video_id'))
	return trailer(video_id)

if __name__ == '__main__' :
        app.run()
