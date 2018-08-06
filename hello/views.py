import json
import os
from os import environ
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

SLACK_API_TOKEN = environ.get('SLACK_API_TOKEN', None)
SLACK_BOT_TOKEN = environ.get('SLACK_BOT_TOKEN', None)
slack_client = SlackClient(SLACK_API_TOKEN)
slack_bot = SlackClient(SLACK_BOT_TOKEN)

consumer_key = environ.get('consumer_key', None)
consumer_secret = environ.get('consumer_secret', None)
access_token = environ.get('access_token', None)
access_token_secret = environ.get('access_token_secret', None)

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

def getTrending():
    pass

def getChannel(request):
    ch_event = json.loads(request.body)
    token = ch_event['token']
    channel = ch_event['event']['channel']
    event_text = ch_event['event']['text']
    if "trend" in event_text or "twitter" in event_text:
        slack_client.api_call(
            "chat.postMessage",
            channel=channel,
            text=event_text,
            icon_emoji=':robot_face:'
        )

    #return HttpResponse(ch_event, content_type="text/plain")

@csrf_exempt
def slack(request):
    req = json.loads(request.body)
    token = req['token']
    if os.environ.get("verification_token") == token:
        getChannel(request)
    else:
        pass

    #return HttpResponse("", content_type="text/plain")
