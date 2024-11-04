from django.urls import path
from .views import (
    AllEvents,
    EventDetailView,
    )

# from .views import MockView

urlpatterns = [
    path('core/events/', AllEvents.as_view(), name='event-list'),
    path('core/events/<int:id>/', EventDetailView.as_view(), name='event-detail'),
    
]