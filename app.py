import os.path

from flask import Flask, Response, send_from_directory, redirect

import logging

logging.basicConfig(filename='Logs/bot_random_time_log_10.log', level=logging.DEBUG)

logging.Formatter(
    fmt='%(asctime)s.%(msecs)03d',
    datefmt='%Y-%m-%d,%H:%M:%S'
)

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/<path:path>')
def send_report(path):
    return send_from_directory('Web_Network', path)

@app.route('/')
def home_page():
    return redirect("/home.html")

if __name__ == '__main__':

    app.run(host="localhost", port=50000, debug=True)


