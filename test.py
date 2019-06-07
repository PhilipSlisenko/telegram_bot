from telegram.ext import Updater, CommandHandler, Dispatcher
import telegram
import requests
import re
from flask import Flask, Response, request
import json

url = "https://api.telegram.org/bot867306259:AAFkrgtHGExlWrtjRrOSHzM-4frKNESxL1w/"

app = Flask(__name__)


def process_message(msg):
    chat_id = msg['message']['chat']['id']
    text = msg['message']['text']
    if text == "/start":
        payload = {'chat_id': chat_id, 'text': f"Hello {msg['message']['from']['first_name']}"}
        requests.post(url + 'sendMessage', json=payload)

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        msg = request.get_json()
        process_message(msg)
        print(json.dumps(msg, indent=4, sort_keys=True))
        return Response("Ok", 200)
    else:
        print("test")
        return "<h1>Philip Telegram Bot</h1>"


if __name__ == "__main__":
    # main()
    # print(__name__)
    app.run(debug=True)