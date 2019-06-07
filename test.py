from telegram.ext import Updater, CommandHandler, Dispatcher
import telegram
import requests
import re
from flask import Flask, Response, request
import json

url = "https://api.telegram.org/bot867306259:AAFkrgtHGExlWrtjRrOSHzM-4frKNESxL1w/"

app = Flask(__name__)

def save_json(obj):
    with open('json_response.json', 'w') as f:
        f.write(json.dumps(obj, ensure_ascii=False, indent=4))


def process_message(msg):
    print('processing msg')
    chat_id = msg['message']['chat']['id']
    text = msg['message']['text']
    if text == "/start":
        payload = {'chat_id': chat_id, 'text': f"Hello {msg['message']['from']['first_name']}"}
        requests.post(url + 'sendMessage', json=payload)


def process_query(query):
    print('processing query')
    pass


def process_request(telegram_request):
    if 'message' in telegram_request:
        return process_message(telegram_request)
    if 'inline_query' in telegram_request:
        return process_query(telegram_request)


@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        telegram_request = request.get_json()
        save_json(telegram_request)
        process_request(telegram_request)
        return Response("Ok", 200)
    else:
        print("test")
        return "<h1>Philip Telegram Bot</h1>"


if __name__ == "__main__":
    # main()
    # print(__name__)
    app.run(debug=True)