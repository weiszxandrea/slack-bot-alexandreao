from apscheduler.schedulers.blocking import BlockingScheduler
from hello import views
sched = BlockingScheduler()

# @sched.scheduled_job('interval', minutes=1)
# def timed_job():
#     views.postTrend("CC06NGT8S", views.trends())
#     # print('This job is run every 30 minute.')

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=0)
def scheduled_job():
    views.postTrend("CC06NGT8S", views.trends())
    # print('This job is run every weekday at 5pm.')

sched.start()