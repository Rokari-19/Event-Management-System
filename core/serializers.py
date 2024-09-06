from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id',
            'event_name',
            'event_desc',
            'event_venue',
            'event_start',
            'event_end',
            'event_status',
            'event_img',
            'event_thumb',
            'organizer',
            'event_slug'
        )