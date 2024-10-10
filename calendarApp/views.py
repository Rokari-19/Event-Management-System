from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import EventTracking
from .forms import EventForm

@login_required
def calendar_view(request):
    events = EventTracking.objects.filter(user=request.user)
    return render(request, '<h1>How far AJ</h1>', {'events': events})

@login_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('calendar_view')
    else:
        form = EventForm()
    return render(request, '<h1>How far AJ</h1>', {'form': form})

