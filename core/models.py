from django.db import models
from django.contrib.auth.models import User
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.template.defaultfilters import slugify

# Create your models here.
# for creating organizer slugs



class Organizer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='organizer')
    email = models.EmailField(max_length=50, blank=True, null=True)
    org_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return self.user.username




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
    event_start = models.DateField()
    event_end = models.DateField()
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    event_venue = models.TextField(max_length=120)
    event_status = models.TextField(max_length=50, choices=CHOICES)
    isCompleted = models.BooleanField(default=False)
    event_img = models.ImageField(upload_to='event_img/', blank=True, null=True)
    event_thumb = models.ImageField(upload_to='event_thumb/', blank=True, null=True, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    organizer = models.ForeignKey(Organizer, related_name='events', on_delete=models.CASCADE, blank=True, null=True)
    event_slug = models.SlugField(unique=True, editable=False)

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
    

    def get_absolute_url(self):
        self.org_slug = slugify(self.organizer)
        return f"/{self.org_slug}/{self.event_slug}/"

    
    def save(self, *args, **kwargs):
        # for auto adding slugs from the frontend
        if not self.event_slug:
            self.event_slug = slugify(self.event_name)

        if self.event_img and not self.event_thumb:
            # Generate the thumbnail
            self.event_thumb = self.make_thumbnail(self.event_img)

        super().save(*args, **kwargs)




class Ticket(models.Model):
    pass


# done:
'''
added get_absolute_url
fixed thumbnail bug
categorize all events according to organizers
setup first view for seeing all events.
create organizer views
create organizer
create user roles
fix new bugs
'''

# todo 
'''
setup for postgresdb
create event detail view
prepare axios and test api calls



configure jwt for auth with djoser

create ticket model and migrate
'''