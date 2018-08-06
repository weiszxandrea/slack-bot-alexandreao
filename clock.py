from apscheduler.schedulers.blocking import BlockingScheduler
from hello import views
from hello.views import slack_bot, get_trending

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    slack_bot.api_call(
         "chat.postMessage",
         channel="CBXF4AC7J",
         text=get_trending(),
         icon_emoji=':robot_face:'
     )


# @sched.scheduled_job('cron', day_of_week='mon-sun', hour=0)
@sched.scheduled_job('cron', day_of_week='mon-sun', hours=8)
def scheduled_job():
    slack_bot.api_call(
        "chat.postMessage",
        channel="CBXF4AC7J",
        text=get_trending(),
        icon_emoji=':robot_face:'
    )


sched.start()