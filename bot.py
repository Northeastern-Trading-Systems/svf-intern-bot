# imports
import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from slackeventsapi import SlackEventAdapter


env_path = Path('.') / 'env'  # denotes where path for the file is so we can load it
load_dotenv(dotenv_path=env_path)

app = Flask(__name__)
# signing secret, route for where events are sent, webserver we send to
slack_event_adapter = SlackEventAdapter('3cc5f9d50eeb60a27396f344565d1b9f', '/slack/events', app)

# token concealed from github
# client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
client = slack.WebClient(token='xoxb-4152885456631-4167497398114-Vcfc7urbc0GZ0QfAMstskDfJ')

client.chat_postMessage(channel='#svf-slack-bot', text='Hello World')

if __name__ == '__main__':
    app.run(debug=True)  # default port 5000, debug = if we modify, flask will auto-modify the deployed file