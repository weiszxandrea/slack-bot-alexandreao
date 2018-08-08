from apscheduler.schedulers.blocking import BlockingScheduler
from hello.views import slack_bot, get_trending

sched = BlockingScheduler()

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