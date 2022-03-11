from datetime import datetime
from app import*
from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler()
# Schedule job_function to be called every 10 seconds
sched.add_job(example, 'interval',seconds=10)
sched.start()
