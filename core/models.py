from django.db import models
from django.contrib.auth.models import User
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.template.defaultfilters import slugify

# Create your models here.


# Events data model
class Event(models.Model):
    CHOICES = (
        ("In Progress", "in progress"),
        ("Canceled", "canceled"),
        ("Scheduled", "scheduled"),
        ("Closed", "closed"),
        ("On-Hold", "on-hold"),
        ("Completed", "completed"),
        ("Stopped", "stopped")
    )
    event_name = models.CharField(max_length=120)
    event_desc = models.TextField(max_length=300, blank=True, null=True)
    event_start = models.DateTimeField()
    event_end = models.DateTimeField()
    event_venue = models.TextField(max_length=120)
    event_status = models.TextField(max_length=50, choices=CHOICES)
    isCompleted = models.BooleanField(default=False)
    event_img = models.ImageField(upload_to='event_img/', blank=True, null=True)
    event_thumb = models.ImageField(upload_to='event_img/', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    organizer = models.ForeignKey(User, related_name='events', on_delete=models.CASCADE)
    event_slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.event_name

    def get_event_thumb(self):
        if self.event_thumb:
            return "http://127.0.0.1:8000" + self.event_thumb.url
        else:
            if self.event_img:
                self.event_thumb = self.make_thumbnail(self.event_img)
                self.save()
                return "http://127.0.0.1:8000" + self.event_thumb.url
            else:
                ''
            

            
    def get_event_img(self):
        if self.event_img:
            return "http://127.0.0.1:8000" + self.event_img.url
        else:
            ''


    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
    

    
    def save(self, *args, **kwargs):
        # for auto adding slugs from the frontend
        if not self.event_slug:
            self.event_slug = slugify(self.event_name)

        super().save(*args, **kwargs)




class Ticket(models.Model):
    pass
