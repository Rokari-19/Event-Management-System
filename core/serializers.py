from rest_framework import serializers

from .models import Event, Organizer, Attendee, User

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

class OrganizerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')

    class Meta:
        model = Organizer
        fields = ['id', 'username', 'org_name', 'email']
        
        
class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = ['username', 'email', 'phone_number', 'address', 'password']




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create_user(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
