import json
import os
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def getTrending():
    pass


def getChannel(request):
    ch_event = json.loads(request.body)
    token = ch_event['token']
    channel = ch_event['event']['channel']
    event_text = ch_event['event']['text']
    if "trend" in event_text or "twitter" in event_text:
        pass

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
