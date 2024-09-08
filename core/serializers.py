from rest_framework import serializers

from .models import Event, Organizer


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
            'start_time',
            'end_time',
            'event_img',
            'event_thumb',
            'organizer',
            'get_absolute_url',
        )

class OrganizerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')

    class Meta:
        model = Organizer
        fields = ['id', 'username', 'org_name', 'email']