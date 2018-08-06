import json
import os
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def slack(request):
    req = json.loads(request.body)
    token = req['token']
    if os.environ.get("verification_key") == token:
        challenge = req['challenge']
    else:
        challenge = "Empty challenge"

    return HttpResponse(challenge, content_type="text/plain")

