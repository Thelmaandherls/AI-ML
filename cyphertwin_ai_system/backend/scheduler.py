from apscheduler.schedulers.background import BackgroundScheduler
import subprocess 
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.combining import OrTrigger


def run_langflow_agent():
    subprocess.run(['python', 'run_agent.py'])

scheduler = BackgroundScheduler()

trigger = OrTrigger([
    CronTrigger
])
scheduler.add_job(run_langflow_agent, 'interval', hours=1)
scheduler.start()
