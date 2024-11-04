from rest_framework import serializers

from .models import Event

# from rest_framework import serializers
# from .models import CustomUser

class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.CharField(source='organizer.org_name', read_only=True)
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
            'organizer',
            'get_absolute_url',
            'get_event_img',
            'get_event_thumb',
            'location',
        )
        
class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'event_img',
        )
        
