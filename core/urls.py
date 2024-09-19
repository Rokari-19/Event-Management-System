from django.urls import path
from .views import AllEvents, OrganizerEventsList, OrganizerListView
from .views import MockView

urlpatterns = [
    path('events/', AllEvents.as_view()),
    path('organizers/<str:organizer_name>/events/', OrganizerEventsList.as_view()), 
    path('organizers/', OrganizerListView.as_view()),
    # this is the routing for the organizer details view
    path('^jwt/$', MockView.as_view()),
    path('^auth-token/$', 'jwt_auth.views.obtain_jwt_token')


]