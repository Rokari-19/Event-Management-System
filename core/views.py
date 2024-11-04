from django.shortcuts import render
from .models import Event, Organizer  
from .serializers import EventSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

class AllEvents(APIView):
    def get(self, request, format=None):
        event = Event.objects.all()
        serializer = EventSerializer(event, many=True)

        return Response(serializer.data)
    

class NewEvent(generics.CreateAPIView):
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
     

'''for use later, incase djoser or simplejwt is needed again'''

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
