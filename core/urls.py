from django.urls import path
from .views import AllEvents

urlpatterns = [
    path('events/', AllEvents.as_view()),
]