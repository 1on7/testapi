from flask import Flask, request
import schedule
import time as t
import _thread as thread
from trailer import trailer
from info import data_info
from search import data_search
from movies import mv
app = Flask(__name__)
def rescrap():
        return mv()
def ref():
        schedule.every().day.at("12:00").do(rescrap)
        while True:
                     schedule.run_pending()
                     t.sleep(1)
thread.start_new_thread(ref, ())
@app.route("/movie", methods=['POST', 'GET'])
def movies():
        return mv()
@app.route("/info", methods=['POST', 'GET'])
def info():
      uid = str(request.args.get('id'))
      return data_info(uid)
@app.route("/search", methods=['POST', 'GET'])
def search():
      name = str(request.args.get('name'))
      return data_search(name)
@app.route("/trailer/", methods=['POST', 'GET'])
def tr():
	video_id = str(request.args.get('video_id'))
	return trailer(video_id)
app.run()
