from django.shortcuts import render
from .models import *
from .serializers import EventSerializer, OrganizerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import status

# Create your views here.
class AllEvents(APIView):
    def get(self, request, format=None):
        event = Event.objects.all()
        serializer = EventSerializer(event, many=True)

        return Response(serializer.data)
    

class NewEvent(APIView):
     def post(self, request, format=None):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     



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

