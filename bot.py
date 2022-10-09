# imports
import random
from typing import Tuple
import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request
import slack_sdk
from slackeventsapi import SlackEventAdapter
from commands import *
import threading
import requests

from commands.analyst_recommendations import Analyst_Recommendations
from commands.cf import Cash_Flow
from commands.dcf import DCF
#from commands.er_implied_move import ER_Implied_Move
from commands.er_info import ER_Info
from commands.f_data import Fundamental_Data
from commands.heatmap import Heatmap
from commands.income import Income_Stmt
from commands.insiders import Insiders
from commands.menu import Menu
from commands.news import News
from commands.overview import Overview
from commands.portfolio_holdings import Portfolio_Holdings
from commands.price_target import Price_Target
from commands.quote import Quote
from commands.technical_analysis import Technical_Analysis
from commands.shareholders import Shareholders
from commands.analysis import Analysis
from commands.candle import Candle

# denotes where path for the file is so we can load it
env_path = Path('.') / 'env'
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)

slack_event_adapter = SlackEventAdapter(
    '8f57d4585beb8feaf5f5876d536930a9', '/slack/events', app)
client = slack.WebClient(token=os.environ['TOKEN_ID'])
client.chat_postMessage(channel='#svf-slack-bot', text='Testing again')


"""
Event method:
When an event occurs in a channel, this method is triggered.
Method echoes the string message that triggered the event.
"""
# TODO: Subscribe to all events in a #intern channel and listen for messages that start with '!intern'

BOT_ID = client.api_call('auth.test')['user_id']  # obtains the id of the bot

"""
STORAGE OF KNOWN COMMANDS THAT CAN BE EXECUTED BY THE INTERN...
"""
known_commands = {
    'menu': Menu(),
    'quote': lambda arr: Quote(*arr),
    'news': lambda arr: News(*arr),
    'ta': lambda arr: Technical_Analysis(*arr),
    'heatmap': Heatmap(),
    'dcf': lambda arr: DCF(*arr),
    'insiders': lambda arr: Insiders(*arr),
    'overview': lambda arr: Overview(*arr),
    'er': lambda arr: ER_Info(*arr),
    'analyst': lambda arr: Analyst_Recommendations(*arr),
    'pt': lambda arr: Price_Target(*arr),
    'port': Portfolio_Holdings(),
    'fd': lambda arr: Fundamental_Data(*arr),
    'cf': lambda arr: Cash_Flow(*arr),
    'income': lambda arr: Income_Stmt(*arr),
    'shrs': lambda arr: Shareholders(*arr),
    'analysis': lambda arr: Analysis(*arr),
    'candle': lambda arr: Candle(*arr),
}


@slack_event_adapter.on('message')
def message(payload):
    # look for 'event' in payload, if it is not found then return an empty dict
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')
    msg_arr = text.split()

    slack_request = request.form

    processor = threading.Thread(
        target=process_event,
        args=(slack_request, channel_id, user_id, msg_arr,)
    )
    processor.start()
    return "Preparing chat response... please wait"


def process_event(slack_request, channel_id, user_id, msg_arr):
    if BOT_ID != user_id:
        if msg_arr[0] == "!intern":
            try:
                command = known_commands.get(msg_arr[1])
                if not command:
                    client.chat_postMessage(
                        channel=channel_id, text="Command not found... Please try again.")
                else:
                    try:
                        if len(msg_arr) > 2:
                            cmd_object = command(msg_arr[2:])
                        else:
                            cmd_object = command
                        response = cmd_object.execute()
                        if type(response) == str:
                            client.chat_postMessage(
                                channel=channel_id, text=response)
                        else:
                            if response[0] == "IMG":
                                try:
                                    client.files_upload(
                                        file=response[1], channels=channel_id)
                                except slack_sdk.errors.SlackRequestError as e:
                                    client.chat_postMessage(
                                        channel=channel_id,
                                        text="Image upload failed, please contact bot admins."
                                    )
                            elif response[0] == "XLSX":
                                try:
                                    client.files_upload(
                                        file=response[1], channels=channel_id)
                                except slack_sdk.errors.SlackRequestError as e:
                                    client.chat_postMessage(
                                        channel=channel_id,
                                        text="Excel sheet upload failed, please contact bot admins.",
                                    )
                            else:
                                client.chat_postMessage(
                                    channel=channel_id, text="Error compiling command... Please try again.")
                    except Exception as e:
                        client.chat_postMessage(
                            channel=channel_id, text=f"Error compiling command... Please try again. {e}")
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

    client.chat_postMessage(
        channel=channel_id, text=f'@{user_id}, your random number is {rand}.')
