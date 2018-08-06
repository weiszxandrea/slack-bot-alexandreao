from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()

import hello.views

urlpatterns = [
    url(r'^slack-alexandreao', hello.views.slack, name='slack'),
]
