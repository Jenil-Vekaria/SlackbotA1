import os
from slackclient import SlackClient
import requests
from geotext import GeoText

# CPS-847-Bot Slack
Bot_User_OAuth_Access_Token = 'xoxb-918319805729-920710774465-ZD1asA2FbrTdQiArUp34eHRO'
SLACK_API_TOKEN = Bot_User_OAuth_Access_Token

# Hardcoded SLACK_API_TOKEN
slack_token = SLACK_API_TOKEN
client = SlackClient(slack_token)


def getWeatherInfo(location):
    http = "https://api.openweathermap.org/data/2.5/weather?q=" + \
        location+"&APPID=d875a99a411c3c52d45d763ae33e6bd9&units=metric"
    response = requests.get(http)

    if response.status_code == 200:
        json = response.json()
        temperature = json['main']
        return "Weather in " + location + " is " + str(temperature['temp']) + "°C"
    elif response.status_code == 404:
        return "Invalid city, please try again!"


def say_hello(data):
    userResponse = data['text']

    if userResponse != "":
        city = GeoText(userResponse).cities[0]
        weatherResponse = getWeatherInfo(city)

        channel_id = data['channel']
        thread_ts = data['ts']
        user = data['user']

        client.api_call('chat.postMessage',
                        channel=channel_id,
                        text=weatherResponse,
                        thread_ts=thread_ts
                        )


if client.rtm_connect():
    while True:
        for data in client.rtm_read():
            if "type" in data and data["type"] == "message":
                say_hello(data)
else:
    print("Connection Failed")
