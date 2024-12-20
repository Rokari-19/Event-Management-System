from django.db import models
from accounts.models import Organizer, CustomUser
from django.template.defaultfilters import slugify
from django.core.files import File
from PIL import Image
from io import BytesIO
    
class CustomDateTimeField(models.DateTimeField):
    def value_to_string(self, obj):
        val = self.value_from_object(obj)
        if val:
            val.replace(microsecond=0)
            return val.isoformat()
        return ''

class Event(models.Model):
    root_url = 'http://127.0.0.1:8000'
    CHOICES = (
        ("In Progress", "in progress"),
        ("Canceled", "canceled"),
        ("Scheduled", "scheduled"),
        ("Closed", "closed"),
        ("On-Hold", "on-hold"),
        ("Completed", "completed"),
        ("Stopped", "stopped")
    )
    
    LOCATIONS = (
        ('Lagos, Nigeria', 'lagos, Nigeria'),
        ('Calabar, Nigeria', 'Calabar, Nigeria'),
        ('Abuja, Nigeria', 'Abuja, Nigeria'),
        ('Abidjan, Cotè d` ivore', 'Abidjan, Cotè d` ivore'),
        ('Cotè d` ivore', 'Cotè d` ivore'),
        ('Capetown, SA', 'Capetown, SA'),
        ('Johanesburg, SA', 'Johanesburg, SA'),
        ('Accra, Ghana', 'Accra, Ghana')
    )
    event_name = models.CharField(max_length=120)
    event_desc = models.TextField(max_length=300, blank=True, null=True)
    event_start = models.DateField()
    event_end = models.DateField()
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    event_venue = models.TextField(max_length=120)
    event_status = models.CharField(max_length=50, choices=CHOICES)
    is_completed = models.BooleanField(default=False)  # Adjusted naming convention
    event_img = models.ImageField(upload_to='image', blank=True, null=True)
    event_thumb = models.ImageField(upload_to='image', blank=True, null=True, editable=False)
    date_created = CustomDateTimeField(auto_now_add=True)
    location = models.CharField(max_length=80, choices=LOCATIONS, blank=True, null=True)
    organizer = models.ForeignKey(Organizer, related_name='events', on_delete=models.CASCADE, blank=True, null=True)
    event_slug = models.SlugField(unique=True, editable=False)

    def __str__(self):
        return self.event_name

    def get_event_thumb(self):
        if self.event_thumb:
            return self.root_url + self.event_thumb.url
        elif self.event_img:
            self.event_thumb = self.make_thumbnail(self.event_img)
            self.save()
            return self.root_url + self.event_thumb.url
        return ''

    def get_event_img(self):
        if self.event_img:
            return self.root_url + self.event_img.url
        return ''

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        thumbnail = File(thumb_io, name=image.name)
        return thumbnail

    def get_absolute_url(self):
        org_slug = slugify(self.organizer.org_name if self.organizer else 'no-organizer')
        return f"/{org_slug}/{self.event_slug}/"

    def save(self, *args, **kwargs):
        if not self.event_slug:
            self.event_slug = slugify(self.event_name)
        if self.event_img and not self.event_thumb:
            self.event_thumb = self.make_thumbnail(self.event_img)
        super().save(*args, **kwargs)


class Ticket(models.Model):
    ticket_name = models.CharField(max_length=50, blank=True, null=True)
    ticket_event = models.ForeignKey(Event, related_name='tickets', on_delete=models.CASCADE)
    ticket_owner = models.ForeignKey(CustomUser, related_name='tickets', on_delete=models.CASCADE)
    date_purchased = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    ticket_number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'Ticket #{self.ticket_number} for {self.ticket_event.event_name}'



# done:
'''
added get_absolute_url
fixed thumbnail bug
categorize all events according to organizers
setup first view for seeing all events.
create organizer views
create organizer
create CustomUser roles
prepare axios and test api calls
reset cors allowed origins
fix new bugs
create ticket model and migrate
create event detail view
wait for djosers to build new auth - scrapped
'''

# todo 
'''
setup for postgresdb
configure jwt for auth with djoser
create log out view
set up google auth
properly configure the datetime class,
for formatting the date and time of events and tickets


    CLEAN UP CODE MESHACH!!!!!!!!
'''


'''
I have some  issues with some db conflicts, can you please help me check it out.
that is the reason why i have not been able to setup the postgresql.
i should be done with this backend by weekend of next weeek.
Thank you my boss
'''

'''
fixed it a while ago meshach
'''