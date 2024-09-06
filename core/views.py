from django.shortcuts import render
from .models import *
from .serializers import EventSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class AllEvents(APIView):
    def get(self, request, format=None):
        event = Event.objects.all()
        serializer = EventSerializer(event, many=True)

        return Response(serializer.data)
