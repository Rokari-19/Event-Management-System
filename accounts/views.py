from django.shortcuts import render
from core.models import Event, Organizer  
from core.serializers import EventSerializer
from .serializers import OrganizerSerializer, UserSerializer, LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions, status
from .models import CustomUser
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated



# Create your views here.
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
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    

class GetCurrentUserView( APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer=self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

class UpdateProfileView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class ForgotPasswordView(APIView):
    def post(self, request):
        email = request.data.get('email')
        # Implement logic to send password reset email
        return Response({'message': 'Password reset email sent'}, status=status.HTTP_200_OK)
