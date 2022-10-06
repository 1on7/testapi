from flask import *
import requests
from bs4 import BeautifulSoup
import schedule as s
import threaded
import time as t
import json
import _thread as thread
from movies import movie, mv_id
app = Flask(__name__)
def rescrap():
        from movies import movie
        print("done")
        return movie()
def ref():
        s.every(12).hours.do(rescrap)
        while True:
                     s.run_pending()
                     t.sleep(1)
thread.start_new_thread(ref, ())
@app.route("/movie", methods=['POST', 'GET'])
def movies():
        return movie()
@app.route("/info/", methods=['POST', 'GET'])
def info():
      id = str(request.args.get('id'))
      data = {'id' : id}
      return data
@app.route("/search/")
def search():
      name = str(request.args.get('name'))
      data = {'name' : name}
      return data
