from django import forms
from .models import EventTracking

class EventForm(forms.ModelForm):
    class Meta:
        model = EventTracking
        fields = ['title', 'description', 'start_time', 'end_time']