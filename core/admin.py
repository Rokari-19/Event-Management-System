from django.contrib import admin
from .models import Event, Organizer, Attendee, Ticket
# Register your models here.

admin.site.register(Event)
admin.site.register(Organizer)
admin.site.register(Attendee)
admin.site.register(Ticket)
