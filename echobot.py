import os
from slackclient import SlackClient

client = SlackClient('<slackbot token>')

def say_hello(data):
    try:
        textData = data['text']

        if "<" in textData and ">" in textData:
            channel_id = data['channel']
            thread_ts = data['ts']
            user = data['user']

            client.api_call('chat.postMessage',
                channel=channel_id,
                text=textData,
                thread_ts=thread_ts
                )
    except:
        print("")

if client.rtm_connect():
    while client.server.connected is True:
        for data in client.rtm_read():
            if "type" in data and data["type"] == "message":
                say_hello(data)
else:
    print("Connection Failed")
