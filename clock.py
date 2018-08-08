import os

from apscheduler.schedulers.blocking import BlockingScheduler
from hello.views import slack_bot, get_trending

sched = BlockingScheduler()

hostname = "google.com"
response = os.system("ping -c 1 " + hostname)

#stops the bot from idling
@sched.scheduled_job('interval', minutes=5)
def timed_job():
    if response == 0:
        print ('bot is active')
    else:
        print ('bot is sleeping')

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
sched.start()
