import os
from slackclient import SlackClient
import requests
from geotext import GeoText


client = SlackClient('<TOKEN>')


def getWeatherInfo(location):
    http = "https://api.openweathermap.org/data/2.5/weather?q=" + \
        location+"&APPID=<OpenWeatherAPIKey>&units=metric"
    response = requests.get(http)

    if response.status_code == 200:
        json = response.json()
        temperature = json['main']
        weatherDescription = json['weather'][0]
        print(weatherDescription)
        return "It will be " + weatherDescription['description'] + " in " + location + " with temperature of " + str(temperature['temp']) + "°C"
    elif response.status_code == 404:
        return "Invalid city, please try again!"


def say_hello(data):
    try:
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
    except:
        print("")


if client.rtm_connect():
    while True:
        for data in client.rtm_read():
            if "type" in data and data["type"] == "message":
                say_hello(data)
else:
    print("Connection Failed")
