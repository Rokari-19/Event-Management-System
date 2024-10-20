from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Event
from django.utils import timezone

@shared_task
def send_event_reminders():
    events = Event.objects.filter(start_time__gte=timezone.now(), reminder_sent=False)
    for event in events:
        if event.should_send_reminder():
            send_mail(
                f"Reminder: {event.title}",
                f"Your event '{event.title}' starts at {event.start_time}.",
                settings.DEFAULT_FROM_EMAIL,
                [event.user.email],
                fail_silently=False,
            )
            event.reminder_sent = True
            event.save()
    return f"Sent reminders for {events.count()} events"