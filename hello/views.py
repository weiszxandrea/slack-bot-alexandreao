import json
import os
from slackclient import SlackClient
from os import environ
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

oauth_token = environ.get('oauth_token', None)
bot_oauth_token = environ.get('bot_oauth_token', None)
slack_client = SlackClient(oauth_token)
slack_bot = SlackClient(bot_oauth_token)

consumer_key = environ.get('consumer_key', None)
consumer_secret = environ.get('consumer_secret', None)
access_token = environ.get('access_token', None)
access_token_secret = environ.get('access_token_secret', None)

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

def getTrending():

    WOE_ID = 1
    trends = api.trends_place(WOE_ID)

    trends = json.loads(json.dumps(trends, indent=1))

    trendy = []
    for trend in trends[0]["trends"]:
        trendy.append((trend["name"]))

    trending = ', \n'.join(trendy[:10])
    return trending


def getChannel(request):
    ch_event = json.loads(request.body)
    token = ch_event['token']
    channel = ch_event['event']['channel']
    event_text = ch_event['event']['text']
    if "trend" in event_text or "twitter" in event_text:
        slack_client.api_call(
            "chat.postMessage",
            channel=channel,
            text=getTrending(),
            icon_emoji=':robot_face:'
        )
    else:
        slack_client.api_call(
            "chat.postMessage",
            channel=channel,
            text="SORRY",
            icon_emoji=':robot_face:'
        )

    return ""

@csrf_exempt
def slack(request):
    req = json.loads(request.body)
    token = req['token']
    if os.environ.get("verification_token") == token:
        getChannel(request)
    else:
        pass

    # return HttpResponse("", content_type="text/plain")
    return request
