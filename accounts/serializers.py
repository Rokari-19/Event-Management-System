from rest_framework import serializers
from .models import Organizer, Attendee, CustomUser
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
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
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create_user(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=6)
    password = serializers.CharField(max_length=68, write_only=True)
    
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'email',
            'password',
        ]
        
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        request = self.context.get('request')
        user = authenticate(request, email=email, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return {'token': token.key}
        else:
            raise serializers.ValidationError('invalid Credentials')