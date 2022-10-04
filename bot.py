# imports
import random
import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request
from slackeventsapi import SlackEventAdapter

env_path = Path('.') / 'env'  # denotes where path for the file is so we can load it
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
# signing secret, route for where events are sent, webserver we send to
slack_event_adapter = SlackEventAdapter('3cc5f9d50eeb60a27396f344565d1b9f', '/slack/events', app)

# token concealed from github
# client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
client = slack.WebClient(token='xoxb-4152885456631-4167497398114-ySKWpbX3YfH4dvCvg48Jn8aG')
BOT_ID = client.api_call('auth.test')['user_id']  # obtains the id of the bot

"""
Event method:

When an event occurs in a channel, this method is triggered.
Method echoes the string message that triggered the event.
"""
@slack_event_adapter.on('message')
def message(payload):
    event = payload.get('event', {})  # look for 'event' in payload, if it is not found then return an empty dict
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')

    if BOT_ID != user_id:
        client.chat_postMessage(channel=channel_id, text=text)  # echoes the message sent to the bot

"""
Command method:

When user calls /get-random in slack, the bot will return a message:
@<user>, your random number is <random num>.
"""
@app.route('/get-random', methods=['POST'])
def get_random():
    data = request.form
    user_id = data.get('user_id')
    channel_id = data.get('channel_id')
    rand = random.random()

    client.chat_postMessage(channel=channel_id, text=f'@{user_id}, your random number is {rand}.')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)  # default port 5000, debug = if we modify, flask will auto-modify the deployed file