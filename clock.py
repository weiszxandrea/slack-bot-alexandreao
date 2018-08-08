import os
import urllib2
from apscheduler.schedulers.blocking import BlockingScheduler
from hello.views import slack_bot, get_trending

sched = BlockingScheduler()

#stops the bot from idling
hostname = urllib2.urlopen("https://slack-bot-alexandreao.herokuapp.com/").read()
response = os.system("ping -c 1 " + hostname)

@sched.scheduled_job('interval', minutes=15)
def timed_job():
    if response == 0:
        print (hostname+' is up!')
    else:
        print (hostname+' is down!')


@sched.scheduled_job('interval', minutes=10)
def timed_job():
    slack_bot.api_call(
        "chat.postMessage",
        channel="CC3NYU3LM",
        text=get_trending(),
        icon_emoji=':robot_face:'
    )

"""
@sched.scheduled_job('cron', day_of_week='mon-sun', hours=9)
def scheduled_job():
    slack_bot.api_call(
        "chat.postMessage",
        channel="CC3NYU3LM",
        text=get_trending(),
        icon_emoji=':robot_face:'
    )

"""
while (True):
    sched.start()
