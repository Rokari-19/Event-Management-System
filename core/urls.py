from django.urls import path
from .views import (
    AllEvents,
    OrganizerEventsList,
    OrganizerListView,
    EventDetailView,
    LoginView,
    SignupView,
    UpdateProfileView,
    ForgotPasswordView,
    )

# from .views import MockView

urlpatterns = [
    path('events/', AllEvents.as_view(), name='event-list'),
    path('organizers/<str:organizer_name>/events/', OrganizerEventsList.as_view()), 
    path('organizers/', OrganizerListView.as_view(), name='organizer-list'),
    path('events/<int:id>/', EventDetailView.as_view(), name='event-detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('update/', UpdateProfileView.as_view(), name='update'),
    path('reset-password/', ForgotPasswordView.as_view(), name='forgot password'),
]