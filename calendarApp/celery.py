from celery import Celery
from celery.schedules import crontab

app = Celery('your_project_name')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Schedule the reminder task to run every hour
app.conf.beat_schedule = {
    'send-hourly-reminders': {
        'task': 'calendar_app.tasks.send_event_reminders',
        'schedule': crontab(minute=0, hour='*'),
    },
}
