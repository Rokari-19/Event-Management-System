from django.shortcuts import render
from .models import *
from .serializers import EventSerializer, OrganizerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

# Create your views here.
class AllEvents(APIView):
    def get(self, request, format=None):
        event = Event.objects.all()
        serializer = EventSerializer(event, many=True)

        return Response(serializer.data)
    
class OrganizerEventsList(generics.ListAPIView):
    serializer_class = EventSerializer


    def get_queryset(self):
            organizer_name = self.kwargs.get('organizer_name')
            if organizer_name:
                # Fetch the organizer by their name (assuming unique name or username)
                organizer = Organizer.objects.get(user__username=organizer_name)
                # Filter events by this organizer
                return Event.objects.filter(organizer=organizer)
            return Event.objects.none()
    
class OrganizerListView(generics.ListAPIView):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer

