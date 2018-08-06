import json
import os

from django.http import HttpResponse
from tweepy import OAuthHandler, API
from slackclient import SlackClient
from os import environ
from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse

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


def get_trending():
    woe_id = 1
    trends = api.trends_place(woe_id)

    trends = json.loads(json.dumps(trends, indent=1))

    trend_temp = []
    for trend in trends[0]["trends"]:
        trend_temp.append((trend["name"]))

    trending = ', \n'.join(trend_temp[:10])
    return trending


def get_channel(request):
    ch_event = json.loads(request.body)
    channel = ch_event['event']['channel']
    event_text = ch_event['event']['text']
    if "trend" in event_text or "twitter" in event_text:
        slack_bot.api_call(
            "chat.postMessage",
            channel=channel,
            text=get_trending(),
            icon_emoji=':robot_face:'
        )
    else:
        slack_client.api_call(
            "chat.postMessage",
            channel=channel,
            text="Sorry your request cannot be processed",
            icon_emoji=':robot_face:'
        )

    return ""


@csrf_exempt
def slack(request):
    req = json.loads(request.body)
    token = req['token']
    if os.environ.get("verification_token") == token:
        get_channel(request)
    else:
        pass

    return HttpResponse(request)
    # return request
