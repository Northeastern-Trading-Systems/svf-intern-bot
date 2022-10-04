# imports
import random
import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request
from slackeventsapi import SlackEventAdapter
from commands import *

env_path = Path('.') / 'env'  # denotes where path for the file is so we can load it
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)

slack_event_adapter = SlackEventAdapter('8f57d4585beb8feaf5f5876d536930a9', '/slack/events', app)
client = slack.WebClient(token=os.environ['TOKEN_ID'])
client.chat_postMessage(channel='#svf-slack-bot', text='Testing again')

"""
Event method:
When an event occurs in a channel, this method is triggered.
Method echoes the string message that triggered the event.
"""
# TODO: Subscribe to all events in a #intern channel and listen for messages that start with '!intern'

BOT_ID = client.api_call('auth.test')['user_id']  # obtains the id of the bot

@slack_event_adapter.on('message')
def message(payload):
    event = payload.get('event', {})  # look for 'event' in payload, if it is not found then return an empty dict
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')
    msg_arr = text.split()

    if BOT_ID != user_id:
        if msg_arr[0] == "!intern":
            try:
                command = Command(msg_arr[1:])
                response_text = command.get_result()
                client.chat_postMessage(channel=channel_id, text=response_text)
            except ValueError as e:
                client.chat_postMessage(channel=channel_id, text=str(e))

        

    # # event must be coming from the proper channel
    # if channel_id != '#svf-slack-bot' or BOT_ID == user_id:
    #     return

    # # check if the message is prompting the bot or not
    # if msg_arr[0] == "!intern":
    #     # TODO: Do something with the remainder of the message
    #     client.chat_postMessage(channel=channel_id, text=text)  # echoes the message sent to the bot

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
