from django.urls import path
from .views import *

urlpatterns = [
    path('events/', AllEvents.as_view()),
    path('organizers/<str:organizer_name>/', OrganizerEventsList.as_view()), 
    path('organizers/', OrganizerListView.as_view()),
    path('new-event/', NewEvent.as_view()),
    path('signup-as-organizer/', NewOrganizer.as_view()),
    # this is the routing for the organizer details view
    
]