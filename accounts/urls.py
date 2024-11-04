from django.urls import path
from .views import (
    OrganizerEventsList,
    OrganizerListView,
    LoginView,
    SignupView,
    UpdateProfileView,
    ForgotPasswordView,
    GetCurrentUserView
)


urlpatterns = [
    path('accounts/organizers/<str:organizer_name>/events/', OrganizerEventsList.as_view()), 
    path('accounts/organizers/', OrganizerListView.as_view(), name='organizer-list'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/signup/', SignupView.as_view(), name='signup'),
    path('accounts/update/', UpdateProfileView.as_view(), name='update'),
    path('accounts/reset-password/', ForgotPasswordView.as_view(), name='forgot password'),
    path('accounts/userdetails/', GetCurrentUserView.as_view(), name='currentUser'),
]