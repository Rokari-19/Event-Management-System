from django.shortcuts import render
from .models import Event, Organizer  
from .serializers import EventSerializer, OrganizerSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions, status
from .models import User
from django.views.generic import View
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, HttpResponseBadRequest
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.encoding import smart_str  

# from django.views.generic import View
# from django.core.serializers.json import DjangoJSONEncoder
# from django.http import HttpResponse, HttpResponseBadRequest
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.encoding import smart_str  

# from .compat import json
# from .forms import JSONWebTokenForm 
# from .mixins import JSONWebTokenAuthMixin  

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


class EventDetailView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_object(self):
        event_id = self.kwargs.get('id')
        return get_object_or_404(Event, id=event_id)
     
class NewOrganizer(APIView):
    def post(self, request, format=None):
        serializer = OrganizerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class OrganizerEventsList(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        organizer_name = self.kwargs.get('organizer_name')
        if organizer_name:
            organizer = Organizer.objects.get(user__username=organizer_name)
            return Event.objects.filter(organizer=organizer)
        return Event.objects.none()
    
class OrganizerListView(generics.ListAPIView):
    queryset = Organizer.objects.all()
    serializer_class = OrganizerSerializer


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            return Response({'token': user.auth_token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class ForgotPasswordView(APIView):
    def post(self, request):
        email = request.data.get('email')
        # Implement logic to send password reset email
        return Response({'message': 'Password reset email sent'}, status=status.HTTP_200_OK)



# class ObtainJSONWebToken(View):
#     http_method_names = ['post']
#     error_response_dict = {'errors': ['Improperly formatted request']}
#     json_encoder_class = DjangoJSONEncoder

#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args, **kwargs):
#         return super(ObtainJSONWebToken, self).dispatch(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         try:
#             request_json = json.loads(smart_str(request.body))  # Replaced smart_text with smart_str
#         except ValueError:
#             return self.render_bad_request_response()

#         form = JSONWebTokenForm(request_json)

#         if not form.is_valid():
#             return self.render_bad_request_response({'errors': form.errors})

#         context_dict = {
#             'token': form.object['token']
#         }

#         return self.render_response(context_dict)

#     def render_response(self, context_dict):
#         json_context = json.dumps(context_dict, cls=self.json_encoder_class)

#         return HttpResponse(json_context, content_type='application/json')

#     def render_bad_request_response(self, error_dict=None):
#         if error_dict is None:
#             error_dict = self.error_response_dict

#         json_context = json.dumps(error_dict, cls=self.json_encoder_class)

#         return HttpResponseBadRequest(
#             json_context, content_type='application/json')


# obtain_jwt_token = ObtainJSONWebToken.as_view()


# class MockView(JSONWebTokenAuthMixin, View):
#     def post(self, request):
#         data = json.dumps({'username': request.user.username})
#         return HttpResponse(data)
