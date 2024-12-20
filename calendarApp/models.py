from datetime import timezone
from django.db import models
from accounts.models import CustomUser
from core.models import Event

class EventTracking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    reminder_sent = models.BooleanField(default=False)

    def should_send_reminder(self):
        now = timezone.now()
        reminder_time = self.start_time - timezone.timedelta(hours=24)
        return not self.reminder_sent and now >= reminder_time
    
    

