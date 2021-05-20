from django.shortcuts import render
from .models import event
# Create your views here.
def view_events(request) :
    events = event.objects.all()
    print(events[0].location)
    return render(request, 'view_events.html', {'events': events})

def create_event(request) :
    events = event.objects.all()
    print(events[0].location)
    return render(request, 'view_events.html',)