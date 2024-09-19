from django.shortcuts import render
from .models import Event, Organizer  
from .serializers import EventSerializer, OrganizerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.views.generic import View
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, HttpResponseBadRequest
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.utils.encoding import smart_str  

from .compat import json
from .forms import JSONWebTokenForm 
from .mixins import JSONWebTokenAuthMixin  


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


class ObtainJSONWebToken(View):
    http_method_names = ['post']
    error_response_dict = {'errors': ['Improperly formatted request']}
    json_encoder_class = DjangoJSONEncoder

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ObtainJSONWebToken, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            request_json = json.loads(smart_str(request.body))  # Replaced smart_text with smart_str
        except ValueError:
            return self.render_bad_request_response()

        form = JSONWebTokenForm(request_json)

        if not form.is_valid():
            return self.render_bad_request_response({'errors': form.errors})

        context_dict = {
            'token': form.object['token']
        }

        return self.render_response(context_dict)

    def render_response(self, context_dict):
        json_context = json.dumps(context_dict, cls=self.json_encoder_class)

        return HttpResponse(json_context, content_type='application/json')

    def render_bad_request_response(self, error_dict=None):
        if error_dict is None:
            error_dict = self.error_response_dict

        json_context = json.dumps(error_dict, cls=self.json_encoder_class)

        return HttpResponseBadRequest(
            json_context, content_type='application/json')


obtain_jwt_token = ObtainJSONWebToken.as_view()


class MockView(JSONWebTokenAuthMixin, View):
    def post(self, request):
        data = json.dumps({'username': request.user.username})
        return HttpResponse(data)
