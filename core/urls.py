from django.urls import path
from .views import AllEvents, OrganizerEventsList, OrganizerListView, EventDetailView
# from .views import MockView

urlpatterns = [
    path('events/', AllEvents.as_view()),
    path('organizers/<str:organizer_name>/events/', OrganizerEventsList.as_view()), 
    path('organizers/', OrganizerListView.as_view()),
    path('events/<int:id>/', EventDetailView.as_view(), name='event-detail'),
   
# =======
# from .views import *

# urlpatterns = [
#     path('events/', AllEvents.as_view()),
#     path('organizers/<str:organizer_name>/', OrganizerEventsList.as_view()), 
#     path('organizers/', OrganizerListView.as_view()),
#     path('new-event/', NewEvent.as_view()),
#     path('signup-as-organizer/', NewOrganizer.as_view()),
    
# >>>>>>> afff2532f7107f207a82a35595431094af3fb033
    # # this is the routing for the organizer details view
    # path('^jwt/$', MockView.as_view()),
    # path('^auth-token/$', 'jwt_auth.views.obtain_jwt_token')



]