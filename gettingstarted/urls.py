from django.conf.urls import include, url
from django.urls import path

from django.contrib import admin
admin.autodiscover()

import hello.views

urlpatterns = [
    url(r'^slack-bot-alexandreao', hello.views.slack, name='slack'),
]
