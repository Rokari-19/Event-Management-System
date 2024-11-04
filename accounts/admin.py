from django.contrib import admin

# Register your models here.
from .models import Organizer, Attendee,CustomUser

admin.site.register(Organizer)
admin.site.register(Attendee)
admin.site.register(CustomUser)